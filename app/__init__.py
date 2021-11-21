
"""
This contains the application factory for creating flask application instances.
Using the application factory allows for the creation of flask applications configured 
for different environments based on the value of the CONFIG_TYPE environment variable
"""

from flask import (Flask,
                   render_template,
                   request)

from flask_mail import Mail
# from config import *
from flask_pymongo import PyMongo
# import error_handle
from app.error_handler import internal_error , not_found_error 
from app.api_error_handler import resource_not_found

# from config import Config

mongo = PyMongo()

### Flask extension objects instantiation ###
mail = Mail()

### Application Factory ###

def create_app():

    app = Flask(__name__)

    # Register error-handler
    app.register_error_handler(500,internal_error)
    app.register_error_handler(400,not_found_error)


    # Configure the flask app instance
    # CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    # app.config.from_object(CONFIG_TYPE)

    # Register blueprints
    register_blueprints(app)

    # Initialize flask extension objects
    initialize_extensions(app)

    # Configure logging
    configure_logging(app)

    # Register error handlers
    register_error_handlers(app)

    return app

### All blueprint module registor here #Sales #Inventory #PUrchase #Elec Inventory 
###  Mechnical Inventroy ###

def register_blueprints(app):
    
    from app.sales import sb
    from app.users import ub
    from app.elecInventory import eb
    from app.mechInventory import mb
    from app.payroll import pb
    from app.purchases import pob
    from app.reports import rb
    from app.manufactures import mfb
    from app.stores import ssb

    app.register_blueprint(ub)
    app.register_blueprint(sb, url_prefix='/sales')
    app.register_blueprint(eb, url_prefix='/electronic')
    app.register_blueprint(mb, url_prefix='/mechnical')
    app.register_blueprint(pb, url_prefix='/payroll')
    app.register_blueprint(pob, url_prefix='/purchases')
    app.register_blueprint(rb, url_prefix='/reports')
    app.register_blueprint(mfb, url_prefix='/manufacture')
    app.register_blueprint(ssb, url_prefix='/stores')

def initialize_extensions(app):
    mail.init_app(app)
    # mongo.init_app(app)

def register_error_handlers(app):
    pass

    # app.register_error_handlers(404,page_not_found)
    # app.register_error_handlers(500,internal_server_error)


# at the application level
# not the blueprint level
 
def page_not_found(e):
    # if a request is in our blog URL space
    if request.path.startswith('/blog/'):
        # we return a custom blog 404 page
        return render_template("blog/404.html"), 404
    else:
        # otherwise we return our generic site-wide 404 page
        return render_template("404.html"), 404

def configure_logging(app):
    pass