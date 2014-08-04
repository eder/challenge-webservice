import requests
import json
import httpretty
from flask import Flask
from flask.ext.testing import TestCase
from flask.ext.testing import LiveServerTestCase
import nose
from nose.tools import assert_equals
from app import app, db
from app.mod_api.facebookConsumers import FacebookConsumer
from app.mod_api.userModel import UserModel
import multiprocessing

if __name__ == '__main__':
	nose.runmodule(argv=[__file__,'-vvs','-x','--pdb', 'pdb-failure'],exit=False)
server = multiprocessing.Process(target=app.run)
server.start()
def createUserTest():
	user = { "username": "nome_do_campeao","id": "123",  
	"name": "Nome do Campeao", "gender": "male", "first_name" : "nome",
	"last_name" : "ultimo nome", "locale": "PT_BR"}
	db.session.add(UserModel(user))
	db.session.commit()
createUserTest()	

class MyTest(TestCase):
	def create_app(self):
		return app
	
	def test_create_user_return_201(self):
		# Should return http_status 201 when user is created
		user =  {'facebookId': 1519373651}
		response = requests.post('http://127.0.0.1:5000/person', user)
		self.assertEquals(response.status_code, 201)
		
	def test_delete_user_return_204(self):
		# Should return http_status 204 when user is deleted
		response = requests.delete("http://127.0.0.1:5000/person/123/")
		self.assertEquals(response.status_code, 204)
	
	def test_delete_user_return_404(self):
		# Should return http_status 400 when user not find user
		response = requests.delete("http://127.0.0.1:5000/person/123/")
		self.assertEquals(response.status_code, 404)
	
	def test_list_of_user_return_200(self):
		# Should return http_status 200 with an array in json
		response = requests.get("http://127.0.0.1:5000/person/?limit=1")
		self.assertEquals(len(response.json()['users']), 1)
		db.session.delete(UserModel.query.filter_by(facebookId=1519373651).first())
		db.session.commit()
	@httpretty.activate
	def test_response_facebook_consumer(self):
		server.terminate() # Server Down
		mock = json.dumps({"id": 1 })
		httpretty.register_uri(httpretty.GET, "http://graph.facebook.com/1",body=mock,content_type="application/json")
		assert_equals(mock, json.dumps(FacebookConsumer().user_by_id('1')))
