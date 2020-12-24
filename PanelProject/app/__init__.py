from flask import Flask, render_template, redirect, request, flash, session,jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
import json
from flask_session import Session
from flask_login import LoginManager

app = Flask(__name__)
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")
sess = Session()
sess.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)

from . import sys_users_control, dashboard_control
from .models import sys_users