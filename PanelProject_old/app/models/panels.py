from .. import db , ma
from . import patients

class Panels(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True )
    name = db.Column(db.String(255),nullable = False, unique=True)
    icon = db.Column(db.String(255),nullable =True)
    color = db.Column(db.String(20),nullable =True)
    patients = db.relationship('Patients', secondary='patient_panels')
    category = db.relationship("Category")


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
    source_plant = db.Column(db.Text(), nullable = True)
    source_animal = db.Column(db.Text(), nullable = True)
    source_others = db.Column(db.Text(), nullable = True)
    what_to_do = db.Column(db.Text(), nullable = True)
    source_status = db.Column(db.String(20), nullable = True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    trait_algorithm_info = db.relationship('TraitAlgorithmInfo')

class TraitAlgorithmInfo(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False, autoincrement = True)
    gene = db.Column(db.String(255), nullable = False)
    rs_id = db.Column(db.String(255), nullable = False)
    genotype = db.Column(db.String(255), nullable = False)
    score = db.Column(db.String(255), nullable = False)
    allele = db.Column(db.String(255), nullable = True)
    trait_id = db.Column(db.Integer, db.ForeignKey('traits.id'))
    trait = db.relationship('Traits')

class TraitAlgorithmInfoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = TraitAlgorithmInfo
        include_fk = True
        relationship = True
        fields = ('id', 'gene', 'rs_id', 'genotype' , 'score' , 'allele', 'trait_id')

class TraitsSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Traits
        include_fk = True
        relationship = True
        fields = ('id', 'name', 'icon_img', 'color' , 'about' , 'source_plant', 'source_animal', 'source_others', 'what_to_do', 'source_status', 'trait_algorithm_info')
    trait_algorithm_info = ma.Nested(TraitAlgorithmInfoSchema)

class CategorySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Category
        include_fk = True
        relationship = True
        fields = ('id', 'name', 'icon_img', 'color' , 'about' , 'panel_id', 'tarits')
    tarits = ma.Nested(Traits)

class PanelSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Panels
        include_fk = True
        relationship = True
        fields = ('id', 'name', 'icon', 'color','category')
    category = ma.Nested(CategorySchema)