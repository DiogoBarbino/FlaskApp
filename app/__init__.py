from flask import Flask
from app.routes import register_routes
from app.core.database import db,migrate
from app.models import *


def create_app():
    app = Flask(__name__)

    #Carrega o banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'OFAODHSFNU87V98ASDY978A8BA8S7D9VAHSD89A7SDGAS89DS8'
    db.init_app(app)
    migrate.init_app(app, db)  # Inicializa o Flask-Migrate



    #carrega as rotas
    register_routes(app)

    return app