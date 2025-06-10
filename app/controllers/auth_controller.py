from flask import render_template,request
from app.models import User
from app.core.database import db
class AuthController:
    def __init__(self):
        pass

    def login(self):
        return render_template("auth/login.html")
    def logout(self):
        return render_template("auth/login.html")
    def register(self):
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            password =  request.form.get('password')
            new_user = User(name,email,password)
            db.session.add(new_user)
            db.session.commit()
            return f"Usuário cadastrado com sucesso!<br>{new_user.name}<br>{new_user.email}<br>{new_user.password_hash}"

        return render_template("auth/register.html")

    def forget(self):
        return render_template("auth/forget.html")