from config import db
from models import TypeBuilding


def InsertTypeBuildingsInDB():
    item = TypeBuilding('Небоскрёб')
    db.session.add(item)
    db.session.commit()

    TypeBuildingList = ('Антенная мачта', 'Бетонная башня', 'Радиомачта', 'Гиперболоидная башня',
                        'Дымовая труба', 'Решётчатая мачта', 'Башня', 'Мост')
    for type in TypeBuildingList:
        item = TypeBuilding(type)
        db.session.add(item)
    db.session.commit()
def RunLabTaskQuery():
    query = TypeBuilding.query.filter(TypeBuilding.type.like("%е%"), TypeBuilding.id>3).all()
    print(query)
