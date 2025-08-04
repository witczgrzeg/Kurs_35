from flask import Flask, render_template, request, redirect


users = [
    {
        "name": "Anna",
        "age": 28,
        "email": "anna.kowalska@example.com",
        "city": "Warszawa"
    },
    {
        "name": "Marek",
        "age": 35,
        "email": "marek.nowak@example.com",
        "city": "Kraków"
    },
    {
        "name": "Kasia",
        "age": 22,
        "email": "kasia.zielinska@example.com",
        "city": "Gdańsk"
    },
    {
        "name": "Tomasz",
        "age": 40,
        "email": "tomasz.lewandowski@example.com",
        "city": "Wrocław"
    },
    {
        "name": "Alicja",
        "age": 31,
        "email": "alicja.kwiatkowska@example.com",
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

@app.route("/users", methods=["GET","POST"])
def show_users():
    saldo = 10
    if request.method == "POST":
        form_type= request.form.get("form_type")
        match form_type:
            case "change_price":
                saldo = request.form.get("new_saldo")
            case "add_user":
                new_user = {
                        "name": request.form.get("name"),
                        "age": request.form.get("age"),
                        "email": request.form.get("email"),
                        "city": request.form.get("city")
                        }
                users.append(new_user)
            case "delete_user":
                user_name = request.form.get("delete_name")
                for user in users:
                    if user["name"] == user_name:
                        users.remove(user)
                        break
    return render_template("users.html", users=users, saldo=saldo)

if __name__ == "__main__":
    app.run(debug=True)