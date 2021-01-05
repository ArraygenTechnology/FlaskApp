from .. import db , datetime , ma

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
    panels = db.relationship('Panels', secondary='patient_panels')

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
    submitted_date = db.Column(db.DateTime, default="")
    first_result = db.Column(db.String(255), nullable=True)
    result_status = db.Column(db.String(255), nullable= False, default="Pending")
    technician_status = db.Column(db.String(255), nullable= True)
    technician_status_date = db.Column(db.DateTime, default="")
    physician_note = db.Column(db.Text(), nullable=True)
    include_note = db.Column(db.String(255), nullable= True)
    physician_status = db.Column(db.String(255), nullable= True)
    physician_status_date = db.Column(db.DateTime, default="")
    second_result = db.Column(db.String(255), nullable=True)
    send = db.Column(db.String(255), nullable=True)
    send_date = db.Column(db.DateTime,  default="")
    print_and_issue = db.Column(db.String(255), nullable=True)
    print_and_issue_date = db.Column(db.DateTime,  default="")

class PatientsSchema(ma.Schema):
    class Meta:
        model = Patients

class Patient_panelsSchema(ma.Schema):
    class Meta:
        model = Patient_panels