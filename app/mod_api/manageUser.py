from app import db
import logging
from app.mod_api.userModel import UserModel
from app.mod_api.facebookConsumers import FacebookConsumer
from marshmallow import Serializer, fields

class UserSerializer(Serializer):
	username  =  fields.String()
	facebookId	= fields.Integer()
	name = fields.String()
	gender = fields.String() 
		
class ManageUser():
	def create_user(self,id):
		if	self.get_user_facebook(id)['id']:
			if UserModel.query.filter_by(facebookId=self.get_user_facebook(id)['id']).first():
				logging.info('User found')
				return '', 409
			else:
				db.session.add(UserModel(self.get_user_facebook(id)))
				db.session.commit()
				logging.info('User created with success')
				return '', 201
		else:
			logging.warning('User not found on the Facebook API')
			self.get_user_facebook(id)
	
	def get_user_facebook(self, id):
		return FacebookConsumer().user_by_id(id)
		
	def destroy_user(self, id):
		if UserModel.query.filter_by(facebookId=id).first():
			db.session.delete(UserModel.query.filter_by(facebookId=id).first())
			db.session.commit()
			return '',204
		else:
			return '', 404	
	def list_of_user(self, count):
		user = UserModel.query.limit(count).all()
		return  UserSerializer(user, many=True).data
			
		
		
	