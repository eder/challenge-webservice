import requests
import json
class FacebookConsumer():

    def __init__(self):
        self.end_point = "http://graph.facebook.com/"

    def user_by_id(self,id):
        return self.request(id) 

    def user_by_name(self,name):
        return self.request(name)

    def request(self, params):
		res	=	requests.get(self.end_point + params)
		return self.to_json(res.content)

    def to_json (self,data):
        return  json.loads(data)
