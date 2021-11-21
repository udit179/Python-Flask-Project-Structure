from flask import Blueprint

rb = Blueprint('reports', 
                __name__,
                template_folder='templates',
                static_folder='static',
                static_url_path='/reports/static')  #This Blueprint way to connect js , css file 

from . import views
from . import models