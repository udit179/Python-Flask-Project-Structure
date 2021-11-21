from flask import Flask
from flask_pymongo import PyMongo

app=Flask(__name__)

class Config():
    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"
    DEBUG = True
    TESTING = False
    WTF_CSRF_ENABLED = True

class DevelopmentConfig(Config):
    DEBUG = True

    ## Development data base and other config
    
class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    MAIL_SUPPRESS_SEND = True

    ## Testing DataBase and other config

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    
    # Production DataBase Config