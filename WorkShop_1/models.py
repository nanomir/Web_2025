from config import db
from app import app
import config as cf

class Country(db.Model):
    __tablename__ = 'Country'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cities = db.relationship("City", back_populates="country", cascade='all, delete')

    def __init__(self, name):
        self.name = name

class TypeBuilding(db.Model):
    __tablename__ = 'TypeBuilding'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(50), nullable=False)
    buildings = db.relationship("Building", back_populates="type_building", cascade='all, delete')
    
    def __init__(self, type):
        self.type = type
        
    def __repr__(self):
        return f'\nid: {self.id}, Тип: {self.type}'

class City(db.Model):
    __tablename__ = 'City'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('Country.id'))
    country = db.relationship("Country", back_populates="cities")
    buildings = db.relationship("Building", back_populates="city", cascade='all, delete')

    def __init__(self, name, country_id):
        self.name = name
        self.country_id = country_id

class Building(db.Model):
    __tablename__ = 'Building'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    type_building_id = db.Column(db.Integer, db.ForeignKey('TypeBuilding.id'))
    city_id = db.Column(db.Integer, db.ForeignKey('City.id'))
    year = db.Column(db.Integer)
    height = db.Column(db.Integer)
    
    type_building = db.relationship("TypeBuilding", back_populates="buildings")
    city = db.relationship("City", back_populates="buildings")
    
    def __init__(self, title, type_building_id, city_id, year, height):
        self.title = title
        self.type_building_id = type_building_id
        self.city_id = city_id
        self.year = year
        self.height = height

cf.app.app_context().push()
with cf.app.app_context():
    db.create_all()
