class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"

    DB_NAME = "db"
    DB_USERNAME = "root"
    DB_PASSWORD = ""

    IMAGE_UPLOADS = "/home/arraygen/Desktop/Akshata/AWSProjectPanels/PanelProject/app/static/uploads"

    SESSION_COOKIE_SECURE = True

    SQLALCHEMY_DATABASE_URI = "mysql://root:@localhost/panel_project"
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
