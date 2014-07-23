from flask import Flask, render_template, redirect, request, flash, session
import model
import jinja2

app = Flask(__name__)
app.secret_key = '\xf5!\x07!qj\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03'
app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def index():
    """This is the cover page of the Vinfluence web app."""
    return render_template("index.html")

@app.route("/type/<wine_type>")
def show_wine_type(wine_type):
    varietal_list = model.get_wine_types(wine_type)
    return render_template("/type.html", varietal_object=varietal_list)

@app.route("/varietal/<id>")
def show_varietal_description(id):
    varietal_description = model.get_varietal(id)
    return render_template("/varietal.html", varietal_description=varietal_description)

# @app.route("/login")
# def login():
#     return render_template("login.html")


if __name__ == "__main__":
    app.run(debug = True)