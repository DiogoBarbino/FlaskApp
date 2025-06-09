from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from app.models import load_models

db = SQLAlchemy()
migrate = Migrate()

def init_app(app):
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    load_models()
    migrate.init_app(app, db)  # Inicializa o Flask-Migrate