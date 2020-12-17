from flask import Flask, render_template, redirect, request,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)
login_manager = '' """LoginManager()
login_manager.init_app(app)"""

from . import admin_views, sys_users_db
from .Models import sys_users