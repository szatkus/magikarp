from flask import Flask, render_template
import json
from application import application
import sample
import login
import register
import registration
from beaker.middleware import SessionMiddleware

session_opts = {
    #'session.type': 'ext:memcached',
	'session.type': 'cookie',
	'session.validate_key': 'abc',
    'session.url': '127.0.0.1:5001',
    'session.data_dir': './cache',
	'session.auto': True,
	'session.save_accessed_time': True
}

@application.route('/')
def root():
    return render_template('sample.html')

if __name__ == '__main__':
	application.wsgi_app = SessionMiddleware(application.wsgi_app,session_opts)
	application.run(debug=True, threaded=True, port=5001)
