import datetime
import enum

from mmgmt_server import db

class MmgmtModel(object):
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

   
class Lang(db.Model, MmgmtModel):
    __tablename__ = 'lang'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(96))
    iso_code = db.Column(db.String(10))
    # dishes = db.relationship('Dish', lazy='dynamic')

    def __init__(self, name, iso_code):
        self.name = str(name)
        self.iso_code = str(iso_code)


recipe_dish = db.Table('recipe_dish',
                       db.Column('recipe_id',
                                 db.Integer,
                                 db.ForeignKey('recipe.id')),
                       db.Column('dish_id',
                                 db.Integer,
                                 db.ForeignKey('dish.id'))
)


class Dish(db.Model, MmgmtModel):
    __tablename__ = 'dish'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=True)
    lang_id = db.Column(db.Integer, db.ForeignKey('lang.id'))
    recipes = db.relationship('Recipe', secondary=recipe_dish,
                              backref=db.backref('pages', lazy='dynamic'))


class Recipe(db.Model, MmgmtModel):
    __tablename__ = 'recipe'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=True)
    create_date = db.Column(db.TIMESTAMP(timezone=True),
                            nullable=True,
                            default=datetime.datetime.utcnow)
    amount_units = db.relationship('Amount_Unit',
                                   backref='recipe',
                                   lazy='dynamic')
    

class Amount_Unit(db.Model, MmgmtModel):
    __tablename__ = 'amount_unit'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Float, nullable=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    unit_id = db.Column(db.Integer, db.ForeignKey('unit.id'))


class EUnit(enum.Enum):
    BIG = "big"
    MEDIUM = "medium"
    SMALL = "small"
    CUP = "cup"
    TABLESPOON = "tablespoon"
    TEASPOON = "teaspoon"
    LITER = "liter"
    KILO = "kilo"
    GRAM = "gram"

    
class Unit(db.Model, MmgmtModel):
    __tablename__ = 'unit'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    unit = db.Column(db.Enum(EUnit), nullable=True, default=EUnit.GRAM)
    val_in_gram = db.Column(db.Float, nullable=True)
    ingredient = db.Column(db.Integer, db.ForeignKey('ingredient.id'))
    

class EIngredientReference(enum.Enum):
    ML = "milliliter",
    G = "gram"

    
class Ingredient(db.Model, MmgmtModel):
    __tablename__ = 'ingredient'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    kcal_100 = db.Column(db.Float, nullable=True, default=0.0)
    kj_100 = db.Column(db.Float, nullable=True, default=0.0)
    protein_100 = db.Column(db.Float, nullable=True, default=0.0)
    fat_100 = db.Column(db.Float, nullable=True, default=0.0)
    fat_saturated_100 = db.Column(db.Float, nullable=True, default=0.0)
    carbs_100 = db.Column(db.Float, nullable=True, default=0.0)
    carbs_sugar_100 = db.Column(db.Float, nullable=True, default=0.0)
    salt_100 = db.Column(db.Float, nullable=True, default=0.0)
    fibers_100 = db.Column(db.Float, nullable=True, default=0.0)
    reference_unit = db.Column(db.Enum(EIngredientReference), nullable=True,
                               default=EIngredientReference.G)
    # units = db.relationship('Unit', backref='ingredient', lazy='dynamic')

    def __init__(self
                 , name
                 , kcal_100=0.0
                 , kj_100=0.0
                 , protein_100=0.0
                 , fat_100=0.0
                 , fat_saturated_100=0.0
                 , carbs_100=0.0
                 , carbs_sugar_100=0.0
                 , salt_100=0.0
                 , fibers_100=0.0):
        self.name = name
        self.kcal_100 = kcal_100
        self.kj_100 = kj_100
        self.protein_100 = protein_100
        self.fat_100 = fat_100
        self.fat_saturated_100 = fat_saturated_100
        self.carbs_100 = carbs_100
        self.carbs_sugar_100 = carbs_sugar_100
        self.salt_100 = salt_100
        self.fibers_100 = fibers_100
