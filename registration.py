from application import application
from flask import Flask, render_template, request

@application.route('/registration', methods=['POST'])
def registration():
    return request.form['login']+"<br>"+request.form['password']+"<br>"+request.form['verify_password']+"<br>"+request.form['email'];
