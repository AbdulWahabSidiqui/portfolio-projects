from flask import Flask,render_template, redirect,url_for
from models import db,Cafe
import os
from forms import CafeForm



app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = os.path.join(BASE_DIR, "cafes.db")

app.config["SECRET_KEY"] = "wahab6969"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_URL}"

db.init_app(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cafes")
def cafes():
    all_cafes = Cafe.query.all()
    return render_template("cafes.html",cafes=all_cafes)

@app.route("/add",methods=["GET","POST"])
def add_cafe():

    form = CafeForm()

    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.name.data,
            map_url = form.map_url.data,
            img_url = form.img_url.data,
            location = form.location.data,
            seats = form.seats.data,
            coffee_price = form.coffee_price.data,
            has_wifi = form.has_wifi.data,
            has_sockets = form.has_sockets.data,
            has_toilet = form.has_toilet.data,
            can_take_calls = form.can_take_calls.data,
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("cafes"))
    return render_template("add_cafe.html",form=form)








if __name__ == "__main__":
    app.run(debug=True)