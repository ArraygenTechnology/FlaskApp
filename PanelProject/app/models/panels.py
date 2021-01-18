from .. import db , ma
from . import patients

class Panels(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True )
    name = db.Column(db.String(255),nullable = False, unique=True)
    icon = db.Column(db.String(255),nullable =True)
    color = db.Column(db.String(20),nullable =True)
    patients = db.relationship('Patients', secondary='patient_panels')
    category = db.relationship("Category")

class PanelSchema(ma.SQLAlchemySchema):
    class Meta:
        model =  Panels
        include_fk = True
        relationship = True
        fields = ('id', 'name', 'icon', 'color')

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    icon_img = db.Column(db.String(255), nullable=True)
    color = db.Column(db.String(20), nullable=True)
    panel_id = db.Column(db.Integer, db.ForeignKey('panels.id'))
    tarits = db.relationship("Traits")

class Traits(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    icon_img = db.Column(db.String(255), nullable=True)
    color = db.Column(db.String(20), nullable=True)
    about = db.Column(db.Text(), nullable = True)
    source_plant =  db.Column(db.Text(), nullable = True)
    source_animal =  db.Column(db.Text(), nullable = True)
    source_others =  db.Column(db.Text(), nullable = True)
    what_to_do =  db.Column(db.Text(), nullable = True)
    source_status =  db.Column(db.String(20), nullable = True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    trait_algorithm_info = db.relationship('TraitAlgorithmInfo')

class TraitAlgorithmInfo(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False, autoincrement = True)
    gene = db.Column(db.String(255), nullable = False, unique = True)
    rs_id = db.Column(db.String(255), nullable = False)
    genotype = db.Column(db.String(255), nullable = False)
    score = db.Column(db.String(255), nullable = False)
    allele = db.Column(db.String(255), nullable = True)
    trait_id = db.Column(db.Integer, db.ForeignKey('traits.id'))