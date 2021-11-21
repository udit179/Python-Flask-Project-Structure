from flask import Blueprint

eb = Blueprint('elecInventory', 
                __name__,
                template_folder='templates',
                static_folder='static',
                static_url_path='/elecInventory/static')

from . import views