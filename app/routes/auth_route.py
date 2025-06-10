from flask import Blueprint
from app.controllers import AuthController

auth_bp = Blueprint("auth",__name__,template_folder="../views")

@auth_bp.route("/auth/login",methods=['POST','GET'])
def login():
    return AuthController().login()

@auth_bp.route("/auth/logout",methods=['POST'])
def logout():
    return AuthController().logout()
@auth_bp.route("/auth/register",methods=['POST','GET'])
def register():
    return AuthController().register()

@auth_bp.route("/auth/forget")
def forget():
    return AuthController().forget()