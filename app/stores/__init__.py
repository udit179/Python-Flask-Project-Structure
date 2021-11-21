from flask import Blueprint

ssb = Blueprint('stores', 
                __name__,
                template_folder='templates',
                static_folder='static',
                static_url_path='/stores/static')

from . import views