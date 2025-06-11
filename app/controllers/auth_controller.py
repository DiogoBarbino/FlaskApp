from flask import render_template,request,redirect,url_for, flash,session
from app.models import User
from app.core.database import db

class AuthController:
    def __init__(self):
        pass

    def login(self):
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')

            user = User.query.filter_by(email=email).first()

            # Verifica se o usuário existe e a senha está correta
            if user and user.check_password(password):
                token = user.get_token()
                session['user_token'] = token
                flash('Login realizado com sucesso!', 'success')
                return redirect(url_for('web.dashboard'))  # Página após login
            else:
                flash('Email ou senha incorretos!', 'danger')
        return render_template("auth/login.html")

    def logout(self):
        session.pop('user_token', None)
        return redirect(url_for('auth.login'))

    def register(self):
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            password =  request.form.get('password')
            new_user = User(name,email,password)
            db.session.add(new_user)
            db.session.commit()
            flash('Usuário cadastrado com sucesso!', 'success')
            return f"Usuário cadastrado com sucesso!<br>{new_user.name}<br>{new_user.email}<br>{new_user.password_hash}"

        return render_template("auth/register.html")

    def forget(self):
        return render_template("auth/forget.html")