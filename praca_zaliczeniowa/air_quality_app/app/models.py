from . import db
from datetime import datetime

class AirQuality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100))
    parameter = db.Column(db.String(50))
    value = db.Column(db.Float)
    unit = db.Column(db.String(10))
    date_utc = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
