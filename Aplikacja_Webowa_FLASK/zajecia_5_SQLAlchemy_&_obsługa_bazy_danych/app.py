from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zajecia_25_baza.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

with app.app_context():
    db.create_all()

    #OPERACJA TWORZENIA NOWEGO REKORDU W BAZIE DANYCH
    # user=User(
    #     username='admin',
    #     password='admin123',
    #     first_name='Admin',
    #     last_name='User',
    # )
    # db.session.add(user)
    # db.session.commit()

    users =User.query.all()
    print(users)

if __name__ == '__main__':
    app.run(debug=True)

