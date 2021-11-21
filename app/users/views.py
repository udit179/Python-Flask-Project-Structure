from flask.helpers import send_file
from . import ub 
import bcrypt
from flask import ( render_template,
                    request , 
                    redirect)

# from users import models
# from application.app.folder.file import func_name 

from app.users.models import User , login_mgr , LoginManager
from app.config import DevelopmentConfig , ProductionConfig

###########################################################
####### User Login Management  
###########################################################

@ub.route('/')
def login():
	    return render_template('login.html')

@ub.route('/login', methods=['GET','POST'])
def usrLogin():
		msg='wrong username or password'
		uemail = request.form['inputEmail']
		upass = request.form['inputPass']
		user = DevelopmentConfig.mongo.db.users
		chkUsr = user.find_one({ 'email' : uemail })

		if chkUsr is not None:
				if bcrypt.hashpw(upass.encode('utf-8'), chkUsr['password'].encode('utf-8')) == chkUsr['password'].encode('utf-8'):
						User(chkUsr)
						# login_user(loginUsr)
						return redirect('apps')
				else:
						return render_template('login.html',message=msg)
		return redirect('/',message="Login User Not Found")
	
@ub.route('/signup/',methods=['POST','GET'])
def signup():
    	return render_template('signup.html')
		
@ub.route('/registration',methods=['POST','GET'])
def registration():
		if request.method == 'POST':
			uname = request.form['inputName']
			upass = request.form['inputPass']
			uemail = request.form['inputEmail']
			umobile = request.form['inputMobile']
			usupervisor = request.form['inputSup']
			role = request.form['inputRole']
			dept = request.form['inputDept']
			user = DevelopmentConfig.mongo.db.users
			existing_user = user.find_one({'email': uemail })

			if existing_user is None:
					hashed = bcrypt.hashpw(upass.encode('utf-8'), bcrypt.gensalt())
					string_hashpw=hashed.decode('utf-8')
					user.insert({'email' : uemail, 'password': string_hashpw,'mobile' : umobile,'username':uname,'role':role,'department':dept,'supervisor':usupervisor})
					return render_template("login.html", message="registered succesfully")
		return render_template('signup.html')

###########################################################
####### Project all module apps.html  
###########################################################

@ub.route('/apps',methods=['GET'])
def apps():
		return render_template('apps.html')