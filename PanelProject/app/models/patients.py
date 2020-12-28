from .. import db
from .panels import Panels

class Patients(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    date = db.Column(db.String(64), nullable=False)
    f_name = db.Column(db.String(64), nullable=False)
    l_name = db.Column(db.String(64), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    ethnicity = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.String(20), nullable=False)
    contact_no = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    address = db.Column(db.Text(), nullable=False)
    panels = db.relationship(Panels, secondary='patient_panels')


class Patient_panels(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    patient_id = db.Column(
      db.Integer,
      db.ForeignKey('patients.id'),
      primary_key = True)

    panel_id = db.Column(
       db.Integer,
       db.ForeignKey('panels.id'),
       primary_key = True)