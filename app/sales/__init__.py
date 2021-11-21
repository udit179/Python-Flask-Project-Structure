from flask import Blueprint

sb = Blueprint('sales', 
                __name__,
                template_folder='templates',
                static_folder='static',
                static_url_path='/sales/static')

from . import views
from . import quote
from . import job_card
from . import manuf_status
from . import customers