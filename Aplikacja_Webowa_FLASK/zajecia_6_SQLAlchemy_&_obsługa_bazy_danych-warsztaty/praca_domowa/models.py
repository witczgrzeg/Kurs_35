from datetime import datetime
from extensions import db


class Saldo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False, default=0.0)

    def __repr__(self):
        return f"<Saldo {self.amount}>"


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(100), nullable=False, unique=True)
    cena = db.Column(db.Float, nullable=False)
    ilosc = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"<Product {self.nazwa} ({self.ilosc} szt.)>"


class Historia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    opis = db.Column(db.String(255), nullable=False)
    data = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<Historia {self.data}: {self.opis}>"
