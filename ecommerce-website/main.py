from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, redirect, url_for, session,request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user,logout_user, login_required
from dotenv import load_dotenv
import os
import stripe

load_dotenv()
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ecommerce.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    if isinstance(user_id, User):
        return user_id

    return User.query.get(int(user_id))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(120), nullable=False)

@app.route('/')
def home():
    products = Product.query.all()
    return render_template("index.html", products=products)

@app.route("/add-to-cart/<int:product_id>")
def add_to_cart(product_id):
    cart = session.get("cart",[])

    if product_id not in cart:
        cart.append(product_id)
    session["cart"] = cart

    return redirect(url_for("home"))

@app.route("/cart")
def cart():
    cart = session.get("cart",[])

    products = Product.query.filter(Product.id.in_(cart)).all() if cart else []

    total = sum([p.price for p in products])

    return render_template("cart.html", products=products,total=total)

@app.route("/remove-from-cart/<int:product_id>")
def remove_from_cart(product_id):
    cart = session.get("cart",[])

    if product_id in cart:
        cart.remove(product_id)

    session["cart"] = cart
    return redirect(url_for("cart"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            return "Email address already exists"

        hashed_password = generate_password_hash(password)

        user = User(name=name, email=email, password=hashed_password)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)

            return redirect(url_for("home"))
        return "Invalid username or password"

    return render_template("login.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/checkout")
@login_required
def checkout():
    cart = session.get("cart", [])

    if not cart:
        return redirect(url_for("cart"))

    products = Product.query.filter(Product.id.in_(cart)).all()

    line_items = []

    for product in products:
        line_items.append({
            "price_data": {
                "currency": "usd",
                "product_data": {
                    "name": product.name,
                },
                "unit_amount": int(product.price * 100),
            },
            "quantity": 1,
        })

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        mode="payment",
        success_url=url_for("success", _external=True),
        cancel_url=url_for("cart", _external=True),
    )

    return redirect(checkout_session.url)

@app.route("/success")
def success():
    session.pop("cart", None)

    return """
        <h1>Payment Successful!</h1>
        <p>Thank you for your purchase.</p>
        <a href="/">Continue Shopping</a>
    """


with app.app_context():
    db.create_all()
    with app.app_context():
        db.create_all()

        if Product.query.count() == 0:
            products = [
                Product(
                    name="Classic T-Shirt",
                    description="A comfortable everyday cotton t-shirt.",
                    price=19.99,
                    image="tshirt.jpg",
                ),
                Product(
                    name="Coffee Mug",
                    description="A simple ceramic mug for your favorite drink.",
                    price=12.99,
                    image="mug.jpg",
                ),
                Product(
                    name="Notebook",
                    description="A clean notebook for your ideas and notes.",
                    price=9.99,
                    image="notebook.jpg",
                )
            ]

            db.session.add_all(products)
            db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)