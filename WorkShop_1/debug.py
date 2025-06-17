from config import db
from models import Country, City, Building, TypeBuilding
from sqlalchemy.sql import func

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
    .group_by(TypeBuilding.id)
    ).all()
    #return [query.statement.columns.keys(), query.all()]
    return query

print(get_types_info())