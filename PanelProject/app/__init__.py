from flask import Flask, render_template, redirect, request, flash, session,jsonify, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import json, os, datetime
from werkzeug.utils import secure_filename
from flask_wtf.csrf import CSRFProtect, CSRFError
from flask_marshmallow import Marshmallow
from flask_mail import Mail, Message

csrf = CSRFProtect()

app = Flask(__name__)
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")
csrf.init_app(app)
ma = Marshmallow(app)
db = SQLAlchemy(app)
mail = Mail(app)
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.before_request
def set_session_timeout():
    session.permanent = True
    app.permanent_session_lifetime = datetime.timedelta(minutes=30)

@app.errorhandler(CSRFError)
def csrf_error(reason):
    if "login_id" in session:
        return render_template('bad_request_internal.html', img=("dist/img/400-error.png", "dist/img/404-error-mobile.png"))
    else:
        return render_template('bad_request.html', img=("dist/img/400-error.png", "dist/img/404-error-mobile.png"))

from . import sys_users_control, dashboard_control, patients_control, analysis_control, results_control
from .models import sys_users