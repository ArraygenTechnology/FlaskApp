from .. import db , datetime
from .panels import Panels

class Patients(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    date = db.Column(db.String(64), nullable=False)
    patient_id = db.Column(db.String(20), nullable=False)
    f_name = db.Column(db.String(64), nullable=False)
    l_name = db.Column(db.String(64), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    ethnicity = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.String(20), nullable=False)
    contact_no = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    address = db.Column(db.Text(), nullable=False)
    order_by = db.Column(db.String(20), nullable=False)
    collection_date = db.Column(db.String(20), nullable=False)
    received_date = db.Column(db.String(20), nullable=False)
    report_generated = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    bmi = db.Column(db.Integer, nullable=False)
    allergic_to = db.Column(db.String(255), nullable=True)
    additional1 = db.Column(db.String(255), nullable=True)
    additional2 = db.Column(db.String(255), nullable=True)
    additional3 = db.Column(db.String(255), nullable=True)
    remark = db.Column(db.Text(), nullable=True)
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

    dna_results = db.Column(db.String(255), nullable= True)
    blood_results = db.Column(db.String(255), nullable= True)
    allergy_results = db.Column(db.String(255), nullable= True)
    submitted_date = db.Column(db.DateTime, default=datetime.datetime.now())