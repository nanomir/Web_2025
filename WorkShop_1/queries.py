from config import db
from models import Building, Country, City, TypeBuilding
import csv 

result = (db.session.query(
    Building.title.label("Название"),
    Country.name.label("Страна"),
    City.name.label("Город"),
    Building.year.label("Год"),
    Building.height.label("Высота")
    )
    .select_from(Building)
    .join(City)
    .join(Country)
    .order_by("Год", Building.height.desc())
    .all())

for item in result:
    print(item)
