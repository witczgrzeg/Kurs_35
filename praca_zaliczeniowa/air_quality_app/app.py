# from flask import Flask
#
# app= Flask(__name__)
#
# @app.route("/")
#
# def hello():
#     return "Hello Worold"
#
# @app.route("/hello")
# @app.route("/hello/<name>")
# def hello_user(name=None):
#     if name:
#         return f"Hello, {name}!"
#     else:
#         return "Hello, User!"
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("main_page.html")

@app.route("/historia")
def historia():
    return render_template("historia.html")

if __name__ == "__main__":
    app.run(debug=True)
