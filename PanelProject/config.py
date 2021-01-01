import os
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'guess'
    UPLOAD_FOLDER = "app/static/uploads"
    SESSION_COOKIE_SECURE = True
    SESSION_PERMANENT = False
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', "csv", "xls", "xlsx"}
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://admin:Arraygen123$@paneldb.cpquggjyqqa1.ap-south-1.rds.amazonaws.com/panel_project"
    #SQLALCHEMY_DATABASE_URI = "mysql://root:@localhost/panel_project"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    pass

class TestingConfig(Config):
    pass
