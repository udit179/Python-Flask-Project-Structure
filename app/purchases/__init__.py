from flask import Blueprint

pob = Blueprint('purchases', 
                __name__,
                template_folder='templates',
                static_folder='static',
                static_url_path='/purchases/static')

from . import views