from flask import Flask, render_template, redirect, request, flash, session
import model
import jinja2
import requests

app = Flask(__name__)
app.secret_key = '\xf5!\x07!qj\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03'
app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def index():
    """This is the cover page of the Vinfluence web app."""
    return render_template("index.html")

@app.route("/type/<wine_type>")
def show_wine_type(wine_type):
    """This is the <type> page. Displays the carousel of various varietals of the wine type selected by user from previous page. """
    varietal_list = model.get_wine_types(wine_type)
    return render_template("/type.html", varietal_object=varietal_list, wine_type=wine_type)

@app.route("/varietal/<id>")
def show_varietal_description(id):
    """This is the <varietal> page. It will display descriptions of the varietal, including food for pairing as well as wine recommendations from the wine.com API."""
    varietal_description = model.get_varietal(id)
#check to see if exist in DB
    # wine_rec_list = 
#else
    api_request = model.make_api_call(id)
    add_api_request_to_db = model.add_api_request_to_db(model.dbsession, api_request, varietal_description)

    return render_template("/varietal.html", varietal=varietal_description, api_request=api_request)

"""Phase 2 feature:
@app.route("/login")
def login():
    return render_template("login.html")
"""
if __name__ == "__main__":
    app.run(debug = True)