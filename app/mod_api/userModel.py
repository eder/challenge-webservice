from app import db
class Users(db.Model):
	facebookId	= db.Column(db.Integer, primary_key = True)
	first_name	=	db.Column(db.String(128))
	last_name = db.Column(db.String(128))
	name = db.Column(db.String(128))
	username = db.Column(db.String(128))
	gender = db.Column(db.String(128))
	link = db.Column(db.String(128))
	locale = db.Column(db.String(128))
 

class UserModel(Users):
    def __init__(self, data):
		self.facebookId	=	data['id']
		self.first_name = data['first_name']
		self.last_name = data['last_name']
		self.name = data['name']
		self.username = data['username']
		self.gender = data['gender']
		self.locale = data['locale']
