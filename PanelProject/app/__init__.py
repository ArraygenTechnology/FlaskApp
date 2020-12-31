from flask import Flask, render_template, redirect, request, flash, session,jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)

from . import sys_users_control, dashboard_control, patients_control, analysis_control
from .models import sys_users