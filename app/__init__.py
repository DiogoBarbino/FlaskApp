from flask import Flask

def create_app():
    app = Flask(__name__)

    #carrega as rotas
    from app.routes.web_route import web_bp
    app.register_blueprint(web_bp)


    return app