from app.routes.web_route import web_bp
from app.routes.auth_route import auth_bp

__all__ = ["web_bp","auth_bp"]

def register_routes(app):
    app.register_blueprint(web_bp)
    app.register_blueprint(auth_bp)