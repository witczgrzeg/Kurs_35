from flask import Flask
from flask_migrate import Migrate
from models import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AirQ.db'
    db.init_app(app)
    migrate = Migrate(app, db)

    from routes import main_page
    app.register_blueprint(main_page)

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
