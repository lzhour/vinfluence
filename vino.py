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

# @app.route("/login")
# def login():
#     return render_template("login.html")

# @app.route("/red")
# def sign_up():
#     return render_template("red.html")

# @app.route("/white")
# def white_wine():
#     """This is the white wine page.""" 
#     return render_template("white.html")

# @app.route("type/<str:varietal_type>")
# def show_wine_type():
# 	  wine_type = model.wine_object
# 	  query the database for one varietal and get some information about
# 	  do something with the data? maybe
#     return render_template("type/<str:varietal_type>.html", data_for_html=datad)


if __name__ == "__main__":
    app.run(debug = True)