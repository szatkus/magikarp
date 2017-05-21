from application import application
from flask import Flask, render_template

@application.route('/login')
def login():
    return render_template('login.html')
