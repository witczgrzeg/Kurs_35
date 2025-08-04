from flask import Flask
from routes import systemks_blueprint

app= Flask(__name__)

app.register_blueprint(systemks_blueprint)

if __name__ == '__main__':
    app.run(debug=True)

