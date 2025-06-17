from app import app
from flask import render_template
from structures.queries_task import get_all_buildings, get_types_info, get_country_info, get_years_info, get_all_buildings_filtered_by_year


@app.route('/')
def index():

    [buildings_head, buildings_body] = get_all_buildings()

    html = render_template(
        'index.html',
        buildings_head=buildings_head,
        buildings_body=buildings_body
    )

    return html

@app.route('/filter')
def filter():

    [buildings_head, buildings_body] = get_all_buildings_filtered_by_year(2000, 2018)

    html = render_template(
        'index.html',
        buildings_head=buildings_head,
        buildings_body=buildings_body
    )

    return html

@app.route('/avg0')
def avg0():

    [buildings_head, buildings_body] = get_types_info()

    html = render_template(
        'index.html',
        buildings_head=buildings_head,
        buildings_body=buildings_body
    )

    return html

@app.route('/avg1')
def avg1():

    [buildings_head, buildings_body] = get_years_info()

    html = render_template(
        'index.html',
        buildings_head=buildings_head,
        buildings_body=buildings_body
    )

    return html

@app.route('/avg2')
def avg2():

    [buildings_head, buildings_body] = get_country_info()

    html = render_template(
        'index.html',
        buildings_head=buildings_head,
        buildings_body=buildings_body
    )

    return html