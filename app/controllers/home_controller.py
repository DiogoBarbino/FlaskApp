from flask import render_template

class HomeController:
    def index(self):
        return render_template('homepage.html')