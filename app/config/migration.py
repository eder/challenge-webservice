from flask import Flask
import sqlalchemy
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from database  import *
engine = sqlalchemy.create_engine(DATABASE_ENG) 
engine.execute("CREATE DATABASE IF NOT EXISTS challengeWebservice_development") 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONF_URI

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Users(db.Model):
	facebookId	= db.Column(db.Integer(), primary_key = True)
	first_name	=	db.Column(db.String(128))
	last_name = db.Column(db.String(128))
	name = db.Column(db.String(128))
	username = db.Column(db.String(128))
	gender = db.Column(db.String(128))
	link = db.Column(db.String(128))
	locale = db.Column(db.String(128))

if __name__ == '__main__':
    manager.run()