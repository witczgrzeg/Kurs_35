from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class LocationCity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(80), nullable=False)
    location_id = db.Column(db.String(80), nullable=True)
    location_name = db.Column(db.String(80), nullable=False)
    sensor_id = db.Column(db.String(80), nullable=False)
    parameter = db.Column(db.String(80), nullable=False)
    value = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.String(80), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('city', 'date', 'parameter', name='uix_city_date_param'),
    )

class SensorMeasurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.String(80), nullable=False)
    parameter = db.Column(db.String(80), nullable=False)
    value = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    units = db.Column(db.String(20), nullable=True)
