from flask import Blueprint

mb = Blueprint('mechInventory', 
                __name__,
                template_folder='templates',
                static_folder='static',
                static_url_path='/mechInventory/static')

from . import views