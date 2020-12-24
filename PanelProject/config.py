import os
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'guess'
    SESSION_TYPE = 'filesystem'
    IMAGE_UPLOADS = "/home/arraygen/Desktop/Akshata/AWSProjectPanels/PanelProject/app/static/uploads"
    SESSION_COOKIE_SECURE = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://admin:Arraygen123$@paneldb.cpquggjyqqa1.ap-south-1.rds.amazonaws.com/panel_project"
    #SQLALCHEMY_DATABASE_URI = "mysql://root:@localhost/panel_project"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = "db"
    DB_USERNAME = "root"
    DB_PASSWORD = ""

    IMAGE_UPLOADS = "/home/arraygen/Desktop/Akshata/AWSProjectPanels/PanelProject/app/static/uploads"

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True

    DB_NAME = "db"
    DB_USERNAME = "root"
    DB_PASSWORD = ""

    SESSION_COOKIE_SECURE = False
