from flask import Blueprint

web_bp = Blueprint("web",__name__,template_folder="views")

@web_bp.route("/")
def homepage():
    return "FlaskApp"