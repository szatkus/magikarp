from application import application
from flask import Flask, render_template, request

@application.route('/registration', methods=['POST'])
def registration():
    return request.form['login'];
