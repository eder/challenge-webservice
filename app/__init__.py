# Import flask and template operators
import logging
logging.basicConfig(filename='logs/development.log',level=logging.DEBUG)
from flask import Flask, jsonify
from  config.database  import *
# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@localhost/challengeWebservice_development'

# Define the database object which is imported
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return '', 404

# # Import a module / 
from app.mod_api.userControllers import mod_api as api_module
# Register blueprint(s)
app.register_blueprint(api_module)

