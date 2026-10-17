from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cafe(db.Model):
    __tablename__ = "cafe"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False,unique=True)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(500), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=False)