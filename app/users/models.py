from flask_login import UserMixin  , LoginManager
from bson.objectid import ObjectId 
from flask import Flask
from app.config import DevelopmentConfig

app=Flask(__name__)

login_mgr = LoginManager(app)
login_mgr.login_view = '/'
login_mgr.login_message = 'You need to be logged in to access the page'
 
class User(UserMixin):
        def __init__(self, user_json):
            if user_json is not None:
                self.id = user_json['_id']
                self.username = user_json['username']
                self.email = user_json['email']
                self.mobile = user_json['mobile']
                self.role = user_json['role']
                self.dept = user_json['department']
                self.supervisor = user_json['supervisor']
		
	# Overriding get_id is required if you don't have the id property
	# Check the source code for UserMixin for details
    
        def get_id(self):
            object_id = self.id
            return str(object_id)

@login_mgr.user_loader
def load_user(user_id):
    users = DevelopmentConfig.mongo.db.users
    user_json = users.find_one({'_id': ObjectId(user_id)})
    return User(user_json) 