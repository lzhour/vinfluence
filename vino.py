from flask import Flask, render_template, redirect, request, flash, session
import model
import jinja2
import requests

app = Flask(__name__)
app.secret_key = '\xf5!\x07!qj\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03'
app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def index():
# This is the cover page of the VinFluence web app.
    return render_template("index.html")

@app.route("/type/<wine_type>")
def show_wine_type(wine_type):
# This is the <type> page -- red or white. Displays a carousel with various varietals associated with the wine type.
    varietal_list = model.get_wine_types(wine_type)
    return render_template("/type.html", varietal_object=varietal_list, wine_type=wine_type)

@app.route("/varietal/<id>")
def show_varietal_description(id):
# This is the <varietal> page. 
# Display descriptions of the varietal, including pairing suggestions and wine recommendations.
# Will first check in db for wine recommendations list to render. If list is empty in database for the selected varietal, will call a function to make an API call to wine.com to retrieve missing data and cache into db. 
    varietal_description = model.get_varietal(id)
    wine_rec_list = model.get_cached_wine_list(varietal_description.varietal)
    if wine_rec_list != []:
        api_request = {}
        api_request["Products"] = {}
        api_request["Products"]["List"] = []
        for wine in wine_rec_list:
            wine_item = {}
            wine_item["Name"] = wine.wine_name
            wine_item["Labels"] = [{"Url": wine.label_image}]
            wine_item["Ratings"] = {"HighestScore": wine.wine_rating}
            wine_item["PriceRetail"] = float(wine.retail_price)
            wine_item["Url"] = wine.wine_url
            api_request["Products"]["List"].append(wine_item)
    else:
        api_request = model.make_api_call(id)
        add_api_request_to_db = model.add_api_request_to_db(model.dbsession, api_request, varietal_description)
   
    return render_template("/varietal.html", varietal=varietal_description, api_request=api_request)

"""Phase 2 feature:"""
@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug = True)