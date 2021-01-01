from flask import Flask, render_template, redirect, request, flash, session,jsonify, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import json, os
from werkzeug.utils import secure_filename

app = Flask(__name__)
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

from . import sys_users_control, dashboard_control, patients_control, analysis_control
from .models import sys_users