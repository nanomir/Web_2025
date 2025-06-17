from app import app
from flask import render_template
from structures.queries_task import get_all_buildings, get_types_info, get_country_info, get_years_info, get_all_buildings_filtered_by_year




@app.route('/')
def index():

    [buildings_head, buildings_body] = get_all_buildings()
    [build_type_head, build_type_body] = get_types_info()
    [build_country_head, build_country_body] = get_country_info()
    [build_year_head, build_year_body] = get_years_info()
    [build_year_bet_head, build_year_bet_body] = get_all_buildings_filtered_by_year(2000,2018)

    html = render_template(
        'index.html',
        buildings_head=buildings_head,
        buildings_body=buildings_body,
        build_type_head=build_type_head,
        build_type_body=build_type_body,
        build_country_head=build_country_head,
        build_country_body=build_country_body,
        build_year_head=build_year_head,
        build_year_body=build_year_body,
        build_year_bet_head=build_year_bet_head,
        build_year_bet_body=build_year_bet_body
    )

    return html