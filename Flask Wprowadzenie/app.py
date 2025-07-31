from flask import Flask, render_template

users = [
    {
        "name": "Anna Kowalska",
        "age": 28,
        "email": "anna.kowalska@example.com",
        "city": "Warszawa"
    },
    {
        "name": "Marek Nowak",
        "age": 35,
        "email": "marek.nowak@example.com",
        "city": "Kraków"
    },
    {
        "name": "Julia Wiśniewska",
        "age": 22,
        "email": "julia.wisniewska@example.com",
        "city": "Gdańsk"
    },
    {
        "name": "Tomasz Wójcik",
        "age": 41,
        "email": "tomasz.wojcik@example.com",
        "city": "Wrocław"
    },
    {
        "name": "Magdalena Zielińska",
        "age": 30,
        "email": "magdalena.zielinska@example.com",
        "city": "Poznań"
    }
]


app= Flask(__name__)

@app.route("/")
def randomowa_nazwa():
    return render_template("hello_worold.html")

def hello():
    return "Hello Worold"

@app.route("/hello")
@app.route("/hello/<name>")
def hello_user(name=None):
    return render_template("hello_user.html", user_name=name)

@app.route("/userrs")
def show_users():
    return render_template("users.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)