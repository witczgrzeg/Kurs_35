from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import main_page
from flask_migrate import Migrate

app = Flask(__name__)
app.register_blueprint(main_page)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AirQ.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class LocationCity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(80), nullable=False)
    location_name = db.Column(db.String(80), unique=True, nullable=False)
    sensor_id = db.Column(db.String(80), nullable=False)
    parameter= db.Column(db.String(80), nullable=False)
    value= db.Column(db.String(80), nullable=False)
    units = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.String(80), nullable=False)



with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)