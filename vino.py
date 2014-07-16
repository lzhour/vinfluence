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


@app.route("/white")
def white_wine():
    """This is the white wine page.""" 
    return redirect("/white")

# @app.route("/varietal")
# def sign_up():
#     return render_template("varietal.html")

# """
# @app.route("/sign_up", methods=["POST"])
# def process_signup():
#     email = request.form.get('email')
#     password = request.form.get('password')
#     age = request.form.get('age')
#     zipcode = request.form.get('zipcode')
#     #print email
#     user_object = model.User(email=email,
#                             password=password,
#                             age=age, 
#                             zipcode=zipcode)
#     #call DB commit function
#     user_object.add_user()
#     #print user_object.id
#     #store userid in browser session and redirect user to logged in page
#     session['userid'] = user_object.id
#     return redirect("/movie_ratings")
# """

if __name__ == "__main__":
    app.run(debug = True)