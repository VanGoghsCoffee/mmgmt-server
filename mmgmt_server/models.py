import datetime
import enum

from mmgmt_server import db

class Lang(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(96))
    iso_code = db.Column(db.String(10))
    dishes = db.relationship('Dish', lazy='dynamic')


recipe_dish = db.Table('recipe_dish',
                       db.Column('recipe_id',
                                 db.Integer,
                                 db.ForeignKey('recipe.id')),
                       db.Column('dish_id',
                                 db.Integer,
                                 db.ForeignKey('dish.id'))
)


class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=True)
    lang_id = db.Column(db.Integer, db.ForeignKey('lang.id'))
    recipes = db.relationship('Recipe', secondary=recipe_dish,
                              backref=db.backref('pages', lazy='dynamic'))


class Recipe(db.Model):
    __tablename__ ='recipe'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=True)
    create_date = db.Column(db.TIMESTAMP(timezone=True),
                            nullable=True,
                            default=datetime.datetime.utcnow)
    amount_units = db.relationship('Amount_Unit',
                                   backref='recipe',
                                   lazy='dynamic')
    

class Amount_Unit(db.Model):
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

    
class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    unit = db.Column(db.Enum(EUnit), nullable=True, default=EUnit.GRAM)
    val_in_gram = db.Column(db.Float, nullable=True)
    ingredient = db.Column(db.Integer, db.ForeignKey('ingredient.id'))
    

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    kcal100 = db.Column(db.Integer, nullable=False)
    protein100 = db.Column(db.Integer, nullable=False)
    fat100 = db.Column(db.Integer, nullable=False)
    carbs100 = db.Column(db.Integer, nullable=False)
    units = db.relationship('Unit', backref='ingredient', lazy='dynamic')
