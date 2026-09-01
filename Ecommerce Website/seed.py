from app import create_app, db
from app.models import Product


app = create_app()


products = [
    {
        "name": "Classic T-Shirt",
        "description": "A comfortable everyday cotton t-shirt.",
        "price": 19.99,
        "image": "tshirt.jpg",
        "category": "Clothing",
        "stock": 50,
    },
    {
        "name": "Coffee Mug",
        "description": "A simple ceramic mug for your favorite drink.",
        "price": 12.99,
        "image": "mug.jpg",
        "category": "Home",
        "stock": 75,
    },
    {
        "name": "Notebook",
        "description": "A clean notebook for your ideas and notes.",
        "price": 9.99,
        "image": "notebook.jpg",
        "category": "Stationery",
        "stock": 100,
    },
]


with app.app_context():
    for product_data in products:
        existing_product = Product.query.filter_by(
            name=product_data["name"]
        ).first()

        if not existing_product:
            product = Product(**product_data)

            db.session.add(product)

    db.session.commit()

    print("Products seeded successfully.")