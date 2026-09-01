from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    session,
    request,
    flash
)
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import stripe
from datetime import datetime
from app import db, login_manager
from app.models import User, Product, Order,OrderItem
import os
from functools import wraps



main = Blueprint("main", __name__)

def admin_required(view):

    @wraps(view)
    def wrapped_view(*args, **kwargs):

        if not current_user.is_authenticated:
            return redirect(url_for("main.login"))

        if not current_user.is_admin:
            return "Access denied", 403

        return view(*args, **kwargs)

    return wrapped_view

def create_order(user, products, cart):
    total = 0

    order = Order(
        user_id=user.id,
        total_amount=0,
        status="Pending",
        created_at=datetime.utcnow()
    )

    db.session.add(order)

    for product in products:

        quantity = cart.get(str(product.id), 0)

        if quantity <= 0:
            continue

        subtotal = product.price * quantity
        total += subtotal

        order_item = OrderItem(
            order=order,
            product_id=product.id,
            quantity=quantity,
            price=product.price
        )

        db.session.add(order_item)

        product.stock -= quantity

    order.total_amount = total

    db.session.commit()

    return order

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@main.route("/")
def home():
    search = request.args.get("search", "").strip()
    category = request.args.get("category", "").strip()

    query = Product.query

    if search:
        query = query.filter(
            Product.name.ilike(f"%{search}%")
        )

    if category:
        query = query.filter_by(category=category)

    products = query.order_by(Product.created_at.desc()).all()

    categories = db.session.query(
        Product.category
    ).distinct().order_by(Product.category).all()

    categories = [category[0] for category in categories]

    return render_template(
        "index.html",
        products=products,
        categories=categories,
        search=search,
        selected_category=category
    )

@main.route("/product/<int:product_id>")
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)

    return render_template(
        "product_detail.html",
        product=product
    )


@main.route("/add-to-cart/<int:product_id>")
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)

    if product.stock <= 0:
        return redirect(url_for("main.home"))

    cart = session.get("cart", {})

    product_id = str(product_id)

    current_quantity = cart.get(product_id, 0)

    if current_quantity < product.stock:
        cart[product_id] = current_quantity + 1

    session["cart"] = cart

    return redirect(request.referrer or url_for("main.home"))


@main.route("/cart")
def cart():
    cart = session.get("cart", {})

    if not cart:
        return render_template(
            "cart.html",
            cart_items=[],
            total=0
        )

    product_ids = [int(product_id) for product_id in cart.keys()]

    products = Product.query.filter(
        Product.id.in_(product_ids)
    ).all()

    cart_items = []

    total = 0

    for product in products:

        quantity = cart.get(str(product.id), 0)

        subtotal = product.price * quantity

        total += subtotal

        cart_items.append({
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal
        })

    return render_template(
        "cart.html",
        cart_items=cart_items,
        total=total
    )
@main.route("/cart/increase/<int:product_id>")
def increase_quantity(product_id):
    product = Product.query.get_or_404(product_id)

    cart = session.get("cart", {})

    product_id = str(product_id)

    current_quantity = cart.get(product_id, 0)

    if current_quantity < product.stock:
        cart[product_id] = current_quantity + 1

    session["cart"] = cart

    return redirect(url_for("main.cart"))
@main.route("/cart/decrease/<int:product_id>")
def decrease_quantity(product_id):

    cart = session.get("cart", {})

    product_id = str(product_id)

    current_quantity = cart.get(product_id, 0)

    if current_quantity > 1:
        cart[product_id] = current_quantity - 1

    elif current_quantity == 1:
        cart.pop(product_id)

    session["cart"] = cart

    return redirect(url_for("main.cart"))

@main.route("/remove-from-cart/<int:product_id>")
def remove_from_cart(product_id):

    cart = session.get("cart", {})

    cart.pop(str(product_id), None)

    session["cart"] = cart

    return redirect(url_for("main.cart"))


@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            return "Email address already exists"

        hashed_password = generate_password_hash(password)

        user = User(
            name=name,
            email=email,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("main.login"))

    return render_template("register.html")


@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)

            return redirect(url_for("main.home"))

        return "Invalid username or password"

    return render_template("login.html")


@main.route("/logout")
def logout():
    logout_user()

    return redirect(url_for("main.home"))

@main.route("/checkout")
@login_required
def checkout():

    cart = session.get("cart", {})

    if not cart:
        return redirect(url_for("main.cart"))

    product_ids = [int(product_id) for product_id in cart.keys()]

    products = Product.query.filter(
        Product.id.in_(product_ids)
    ).all()

    line_items = []

    total = 0

    for product in products:

        quantity = cart.get(str(product.id), 0)

        if quantity <= 0:
            continue

        if quantity > product.stock:
            return (
                f"Not enough stock for {product.name}. "
                f"Only {product.stock} available."
            )

        subtotal = product.price * quantity
        total += subtotal

        line_items.append({
            "price_data": {
                "currency": "usd",
                "product_data": {
                    "name": product.name,
                },
                "unit_amount": int(product.price * 100),
            },
            "quantity": quantity,
        })

    if not line_items:
        return redirect(url_for("main.cart"))

    # Create a pending order
    order = Order(
        user_id=current_user.id,
        total_amount=total,
        status="Pending",
        created_at=datetime.utcnow()
    )

    db.session.add(order)
    db.session.flush()

    # Add products to the order
    for product in products:

        quantity = cart.get(str(product.id), 0)

        if quantity <= 0:
            continue

        order_item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            quantity=quantity,
            price=product.price
        )

        db.session.add(order_item)

    db.session.commit()

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        mode="payment",

        metadata={
            "order_id": str(order.id),
            "user_id": str(current_user.id)
        },

        success_url=url_for(
            "main.success",
            session_id="{CHECKOUT_SESSION_ID}",
            _external=True
        ),

        cancel_url=url_for(
            "main.cart",
            _external=True
        ),
    )

    return redirect(checkout_session.url)

@main.route("/stripe-webhook", methods=["POST"])
def stripe_webhook():
    payload = request.data
    sig_header = request.headers.get("Stripe-Signature")
    endpoint_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            endpoint_secret
        )

    except ValueError:
        print("Webhook error: Invalid payload")
        return "Invalid payload", 400

    except stripe.error.SignatureVerificationError:
        print("Webhook error: Invalid signature")
        return "Invalid signature", 400

    print(f"Stripe event received: {event['type']}")

    if event["type"] == "checkout.session.completed":

        checkout_session = event["data"]["object"]

        metadata = checkout_session.metadata.to_dict()
        order_id = metadata.get("order_id")

        print(f"Webhook order ID: {order_id}")

        if not order_id:
            print("Webhook error: Missing order ID")
            return "Missing order ID", 400

        order = Order.query.get(int(order_id))

        if not order:
            print(f"Webhook error: Order #{order_id} not found")
            return "Order not found", 404

        if order.status != "Paid":

            for item in order.items:

                product = item.product

                if product.stock < item.quantity:
                    print(
                        f"Webhook error: Not enough stock for "
                        f"{product.name}"
                    )
                    return "Not enough stock", 400

                product.stock -= item.quantity

            order.status = "Paid"

            db.session.commit()

            print(f"Order #{order.id} marked as Paid")

    return "", 200

@main.route("/success")
def success():

    session.pop("cart", None)

    return render_template("success.html")

@main.route("/dashboard")
@login_required
def dashboard():

    orders = Order.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Order.created_at.desc()
    ).all()

    total_spent = sum(
        order.total_amount
        for order in orders
        if order.status == "Paid"
    )

    return render_template(
        "dashboard.html",
        orders=orders,
        total_spent=total_spent
    )
@main.route("/orders/<int:order_id>")
@login_required
def order_detail(order_id):

    order = Order.query.filter_by(
        id=order_id,
        user_id=current_user.id
    ).first_or_404()

    return render_template(
        "order_detail.html",
        order=order
    )

@main.route("/admin/orders/<int:order_id>")
@admin_required
def admin_order_detail(order_id):

    order = Order.query.get_or_404(order_id)

    return render_template(
        "admin/order_detail.html",
        order=order
    )
@main.route("/admin")
@admin_required
def admin_dashboard():

    # -------------------------
    # Basic dashboard data
    # -------------------------

    products = Product.query.order_by(
        Product.created_at.desc()
    ).all()

    orders = Order.query.order_by(
        Order.created_at.desc()
    ).all()

    recent_orders = orders[:5]

    users = User.query.order_by(
        User.id.desc()
    ).all()


    # -------------------------
    # Revenue
    # -------------------------

    paid_orders = [
        order
        for order in orders
        if order.status == "Paid"
    ]

    total_revenue = sum(
        order.total_amount
        for order in paid_orders
    )

    average_order_value = (
        total_revenue / len(paid_orders)
        if paid_orders
        else 0
    )


    # -------------------------
    # Stock statistics
    # -------------------------

    low_stock_products = [
        product
        for product in products
        if 0 < product.stock <= 5
    ]

    out_of_stock_products = [
        product
        for product in products
        if product.stock == 0
    ]


    # -------------------------
    # Order statistics
    # -------------------------

    pending_orders = [
        order
        for order in orders
        if order.status == "Pending"
    ]

    fulfilling_orders = [
        order
        for order in orders
        if order.status in ["Processing", "Shipped"]
    ]


    # -------------------------
    # Best-selling products
    # -------------------------

    product_sales = {}

    for order in paid_orders:

        for item in order.items:

            product_id = item.product_id

            if product_id not in product_sales:
                product_sales[product_id] = {
                    "product": item.product,
                    "quantity": 0,
                    "revenue": 0
                }

            product_sales[product_id]["quantity"] += item.quantity

            product_sales[product_id]["revenue"] += (
                item.price * item.quantity
            )


    best_selling_products = sorted(
        product_sales.values(),
        key=lambda x: x["quantity"],
        reverse=True
    )[:5]


    # -------------------------
    # Top customers
    # -------------------------

    customer_sales = {}

    for order in paid_orders:

        user_id = order.user_id

        if user_id not in customer_sales:
            customer_sales[user_id] = {
                "user": order.user,
                "orders": 0,
                "spent": 0
            }

        customer_sales[user_id]["orders"] += 1

        customer_sales[user_id]["spent"] += order.total_amount


    top_customers = sorted(
        customer_sales.values(),
        key=lambda x: x["spent"],
        reverse=True
    )[:5]


    # -------------------------
    # Customer statistics
    # -------------------------

    customer_stats = []

    for user in users:

        user_orders = [
            order
            for order in orders
            if order.user_id == user.id
        ]

        user_paid_orders = [
            order
            for order in user_orders
            if order.status == "Paid"
        ]

        total_spent = sum(
            order.total_amount
            for order in user_paid_orders
        )

        customer_stats.append({
            "user": user,
            "order_count": len(user_orders),
            "total_spent": total_spent
        })


    # -------------------------
    # Render dashboard
    # -------------------------

    return render_template(
        "admin/dashboard.html",

        products=products,
        orders=orders,
        users=users,

        total_revenue=total_revenue,
        average_order_value=average_order_value,

        low_stock_products=low_stock_products,
        out_of_stock_products=out_of_stock_products,

        paid_orders=paid_orders,
        pending_orders=pending_orders,
        fulfilling_orders=fulfilling_orders,

        best_selling_products=best_selling_products,
        top_customers=top_customers,

        customer_stats=customer_stats,
        recent_orders=recent_orders
    )
@main.route("/admin/customers/<int:user_id>")
@admin_required
def admin_customer_detail(user_id):

    user = User.query.get_or_404(user_id)

    orders = Order.query.filter_by(
        user_id=user.id
    ).order_by(
        Order.created_at.desc()
    ).all()

    paid_orders = [
        order
        for order in orders
        if order.status == "Paid"
    ]

    pending_orders = [
        order
        for order in orders
        if order.status == "Pending"
    ]

    total_spent = sum(
        order.total_amount
        for order in paid_orders
    )

    average_order_value = (
        total_spent / len(paid_orders)
        if paid_orders
        else 0
    )

    return render_template(
        "admin/customer_detail.html",
        user=user,
        orders=orders,
        total_spent=total_spent,
        paid_orders=paid_orders,
        pending_orders=pending_orders,
        average_order_value=average_order_value
    )

@main.route("/admin/orders")
@admin_required
def admin_orders():

    status = request.args.get("status", "").strip()

    # Get all orders
    all_orders = Order.query.order_by(
        Order.created_at.desc()
    ).all()

    # Statistics
    total_orders = len(all_orders)

    paid_orders = sum(
        1 for order in all_orders
        if order.status == "Paid"
    )

    pending_orders = sum(
        1 for order in all_orders
        if order.status == "Pending"
    )

    cancelled_orders = sum(
        1 for order in all_orders
        if order.status == "Cancelled"
    )

    # Apply selected filter
    orders = all_orders

    if status:
        orders = [
            order
            for order in all_orders
            if order.status == status
        ]

    return render_template(
        "admin/orders.html",
        orders=orders,
        selected_status=status,
        total_orders=total_orders,
        paid_orders=paid_orders,
        pending_orders=pending_orders,
        cancelled_orders=cancelled_orders
    )

@main.route("/admin/products/add", methods=["GET", "POST"])
@admin_required
def add_product():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()
        price = request.form.get("price", "").strip()
        category = request.form.get("category", "").strip()
        stock = request.form.get("stock", "").strip()
        image = request.form.get("image", "").strip()

        if not all([
            name,
            description,
            price,
            category,
            stock,
            image
        ]):
            return "All fields are required", 400

        try:
            price = float(price)
            stock = int(stock)

        except ValueError:
            return "Price must be a number and stock must be a whole number", 400

        if price < 0 or stock < 0:
            return "Price and stock cannot be negative", 400

        existing_product = Product.query.filter_by(
            name=name
        ).first()

        if existing_product:
            return "A product with this name already exists", 400

        product = Product(
            name=name,
            description=description,
            price=price,
            image=image,
            category=category,
            stock=stock
        )

        db.session.add(product)
        db.session.commit()

        return redirect(url_for("main.admin_dashboard"))

    return render_template("admin/add_product.html")

@main.route("/admin/products/<int:product_id>/edit", methods=["GET", "POST"])
@login_required
@admin_required
def edit_product(product_id):

    product = Product.query.get_or_404(product_id)

    if request.method == "POST":

        product.name = request.form.get("name")
        product.description = request.form.get("description")
        product.price = float(request.form.get("price"))
        product.category = request.form.get("category")
        product.stock = int(request.form.get("stock"))
        product.image = request.form.get("image")

        db.session.commit()

        return redirect(url_for("main.admin_dashboard"))

    return render_template(
        "admin/edit_product.html",
        product=product
    )
@main.route("/admin/products/delete/<int:product_id>", methods=["POST"])
@admin_required
def delete_product(product_id):

    product = Product.query.get_or_404(product_id)

    existing_order_item = OrderItem.query.filter_by(
        product_id=product.id
    ).first()

    if existing_order_item:
        from flask import flash

        flash(
            f"{product.name} cannot be deleted because it has already "
            "been included in an order.",
            "warning"
        )

        return redirect(url_for("main.admin_dashboard"))

    db.session.delete(product)
    db.session.commit()

    from flask import flash

    flash(
        f"{product.name} was deleted successfully.",
        "success"
    )

    return redirect(url_for("main.admin_dashboard"))



@main.route(
    "/admin/orders/<int:order_id>/status",
    methods=["POST"]
)
@admin_required
def update_order_status(order_id):

    order = Order.query.get_or_404(order_id)

    new_status = request.form.get("status", "").strip()

    allowed_statuses = [
        "Pending",
        "Paid",
        "Processing",
        "Shipped",
        "Delivered",
        "Cancelled"
    ]

    if new_status not in allowed_statuses:
        from flask import flash

        flash(
            "Invalid order status.",
            "danger"
        )

        return redirect(
            url_for(
                "main.admin_order_detail",
                order_id=order.id
            )
        )

    order.status = new_status

    db.session.commit()

    from flask import flash

    flash(
        f"Order #{order.id} status updated to {new_status}.",
        "success"
    )

    return redirect(
        url_for(
            "main.admin_order_detail",
            order_id=order.id
        )
    )