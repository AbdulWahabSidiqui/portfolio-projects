from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,IntegerField,DecimalField,SubmitField
from wtforms.validators import DataRequired,URL

class CafeForm(FlaskForm):
    name = StringField("Cafe Name",validators=[DataRequired()])
    map_url = StringField("Map URL",validators=[DataRequired(),URL()])
    img_url = StringField("Image URL",validators=[DataRequired(),URL()])
    location = StringField("Location",validators=[DataRequired()])
    seats = StringField("Number of Seats",validators=[DataRequired()])
    coffee_price = StringField("Coffee Price",validators=[DataRequired()])

    has_wifi = BooleanField("Has WiFi")
    has_sockets = BooleanField("Has Sockets")
    has_toilet = BooleanField("Has Toilet")
    can_take_calls = BooleanField("Can Take Calls")

    submit = SubmitField("Add Cafe")