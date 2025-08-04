from flask import Flask
from routes import my_blueprint
from  views import users_blueprint


app = Flask(__name__)
app.register_blueprint(my_blueprint)
app.register_blueprint(users_blueprint)

if __name__ == '__main__':
    app.run(debug=True)

