from flask import Blueprint

ub = Blueprint('users', 
                __name__,
                template_folder='templates',
                static_folder='static',
                static_url_path='/users/static')  #This Blueprint way to connect js , css file 

from . import views
from . import models