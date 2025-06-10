from os import environ, path
from dotenv import load_dotenv

#Carrega as variaveis do arquivo
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir,'.env'))

class Config:
    #Configurações básicas
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_ENV = environ.get('FLASK_ENV')
    FLASK_APP = environ.get('FLASK_APP')

    #Configurações da base de dados
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True

class ProductionoConfig(Config):
    DEBUG = False
    TESTING = False
