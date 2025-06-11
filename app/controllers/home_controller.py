from flask import render_template,session,redirect,url_for
from app.models import User

class HomeController:
    def index(self):
        return render_template('homepage.html')

    def dashboard(self):
        user_token = session.get('user_token', None)
        if user_token:
            current_user = User.check_token(user_token)
            return render_template('dashboard.html',current_user=current_user)
        return redirect(url_for('auth.login'))