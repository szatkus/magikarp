from application import application
from flask import Flask, render_template

@application.route('/register')
def register():
    return render_template('register.html')
