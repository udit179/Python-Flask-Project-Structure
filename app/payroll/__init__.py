from flask import Blueprint

pb = Blueprint('payroll', 
                __name__,
                template_folder='templates',
                static_folder='static',
                static_url_path='/payroll/static')

from . import views