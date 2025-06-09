from flask import Blueprint

auth_bp = Blueprint("auth",__name__,template_folder="../views")

@auth_bp.route("/auth/login")
def login():
    return "FlaskApp Login"