from flask import Flask
import config

application = Flask('magikarp')
application.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
