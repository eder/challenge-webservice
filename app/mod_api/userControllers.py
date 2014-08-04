#Import flask dependencies
from flask import Blueprint, request, redirect, abort,  jsonify
from app.mod_api.manageUser import ManageUser
mod_api = Blueprint('api', __name__)

# Set the route and accepted methods
@mod_api.route('/person', methods=['POST'])
def create():
	if request.form['facebookId']:
		return ManageUser().create_user(request.form['facebookId'])
	else:
		return abort(403)

@mod_api.route('/person/<facebookId>',  methods=['DELETE'])
def destory(facebookId):
	return ManageUser().destroy_user(facebookId)

@mod_api.route('/person/')
def index():
	limit = request.args.get('limit')
	return  jsonify( { 'users' : ManageUser().list_of_user(limit) } )

	

	

	


