from flask import Blueprint

mfb = Blueprint('manufactures', 
                __name__,
                template_folder='templates',
                static_folder='static',
                static_url_path='/manufactures/static')

from . import views