from config import db 
from models import Country, City, Building, TypeBuilding
from sqlalchemy.sql import func, asc, desc
from sqlalchemy import and_

def get_all_buildings():
    query = (
        db.session.query(
            Building.title.label("Здание"),
            TypeBuilding.type.label("Тип"),
            Country.name.label("Страна"),
            City.name.label("Город"),
            Building.year.label("Год"),
            Building.height.label("Высота")
          )
        .select_from(Building)
        .join(TypeBuilding)
        .join(City)
        .join(Country)
    )
    return [query.statement.columns.keys(), query.all()]

def get_all_buildings_filtered_by_year(bottom_year, top_year):
    query = (
        db.session.query(
            Building.title.label("Здание"),
            TypeBuilding.type.label("Тип"),
            Country.name.label("Страна"),
            City.name.label("Город"),
            Building.year.label("Год"),
            Building.height.label("Высота")
          )
        .select_from(Building)
        .join(TypeBuilding)
        .join(City)
        .join(Country)
        .where(and_(Building.year<=top_year, Building.year>=bottom_year))
        .order_by(asc(Building.year))
    )
    return [query.statement.columns.keys(), query.all()]

def get_years_info():
    query = (
        db.session.query(
    Building.year.label("Год"),
    func.max(Building.height).label('Максимальная высота'),
    func.min(Building.height).label('Минимальная высота'),
    (func.sum(Building.height) / func.count(Building.height)).label('Средняя высота')
    )
    .select_from(Building)
    .group_by(Building.year)
    .order_by(func.max(Building.height))
    )
    return [query.statement.columns.keys(), query.all()]

def get_types_info():
    query = (
        db.session.query(
    TypeBuilding.type.label("Тип"),
    func.max(Building.height).label('Максимальная высота'),
    func.min(Building.height).label('Минимальная высота'),
    (func.sum(Building.height) / func.count(Building.height)).label('Средняя высота')
    )
    .select_from(TypeBuilding)
    .join(Building)
    .group_by(TypeBuilding.type)
    .order_by(func.max(Building.height))
    )
    return [query.statement.columns.keys(), query.all()]

def get_country_info():
    query = (
        db.session.query(
    Country.name.label("Страна"),
    func.max(Building.height).label('Максимальная высота'),
    func.min(Building.height).label('Минимальная высота'),
    (func.sum(Building.height) / func.count(Building.height)).label('Средняя высота')
    )
    .select_from(Building)
    .join(City)
    .join(Country)
    .group_by(Country.name)
    .order_by(func.max(Building.height))
    )
    return [query.statement.columns.keys(), query.all()]
