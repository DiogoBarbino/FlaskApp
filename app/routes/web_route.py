from flask import Blueprint
from app.controllers import HomeController

web_bp = Blueprint("web",__name__,template_folder="../views/web")

@web_bp.route("/")
def homepage():
    return HomeController().index()

@web_bp.route("/dashboard")
def dashboard():
    return HomeController().dashboard()

