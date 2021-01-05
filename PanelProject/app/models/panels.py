from .. import db , ma


class Panels(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True )
    name = db.Column(db.String(255),nullable = False, unique=True)
    patients = db.relationship('Patients', secondary='patient_panels')

