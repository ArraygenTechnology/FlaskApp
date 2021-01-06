from .. import db , ma
from . import patients

class Panels(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True )
    name = db.Column(db.String(255),nullable = False, unique=True)
    patients = db.relationship('Patients', secondary='patient_panels')

class PanelSchema(ma.SQLAlchemySchema):
    class Meta:
        model =  Panels
        include_fk = True
        relationship = True
        fields = ('id', 'name')

