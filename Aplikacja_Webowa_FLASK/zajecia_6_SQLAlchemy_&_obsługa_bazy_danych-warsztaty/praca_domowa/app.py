from flask import Flask
from routes import systemks_blueprint
from extensions import db
from models import Saldo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///magazyn.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(systemks_blueprint)

with app.app_context():
    db.create_all()
    if not db.session.query(Saldo).first():
        default_saldo = Saldo(amount=10000)
        db.session.add(default_saldo)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
