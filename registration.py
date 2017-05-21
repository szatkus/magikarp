from application import application
from flask import Flask, render_template, request
from beaker.middleware import SessionMiddleware

@application.route('/registration', methods=['POST'])
def registration():
	result = '';
	session = request.environ['beaker.session'];

	if not session.has_key('password'):
		session['password']=request.form['password'];
		session.save();
		result+='Ustawiono ciasteczko<br>';
		result+='Wartosc ciasteczka: '+session['password'];
	else:
		result+='Odczytano ciasteczko<br>';
		result+='Wartosc ciasteczka: '+session['password'];

	return result;

	#request.form['login']+"<br>"+request.form['password']+"<br>"+request.form['verify_password']+"<br>"+request.form['email'];
