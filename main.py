import json

from flask import request

from config import app
from utils import init_db, get_all, get_model_by_id, insert_data, update_table, delete_data
from models import *


@app.route('/users/', methods=['GET', 'POST'])
def get_all_users():
    if request.method == 'GET':
        data = get_all(User)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data(User, request.json)
        elif isinstance(request.json, dict):
            insert_data(User, [request.json])
        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )


@app.route('/orders/', methods=['GET', 'POST'])
def get_all_orders():
    if request.method == 'GET':
        data = get_all(Order)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data(Order, request.json)
        elif isinstance(request.json, dict):
            insert_data(Order, [request.json])
        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )


@app.route('/offers/', methods=['GET', 'POST'])
def get_all_offers():
    if request.method == 'GET':
        data = get_all(Offer)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data(Offer, request.json)
        elif isinstance(request.json, dict):
            insert_data(Offer, [request.json])
        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )


@app.route('/users/<int:pk>', methods=['GET', 'PUT', 'DELETE'])
def get_users_id(pk):
    if request.method == 'GET':
        data = get_model_by_id(User, pk)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )
    elif request.method == 'PUT':
        update_table(User, pk, request.json)
        return app.response_class(
            response=json.dumps(['Данные успешно обновлены'], indent=4, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )
    elif request.method == 'DELETE':
        delete_data(User, pk)
        return app.response_class(
            response=json.dumps(['Данные успешно удалены'], indent=4, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )


@app.route('/orders/<int:pk>', methods=['GET', 'PUT', 'DELETE'])
def get_orders_id(pk):
    if request.method == 'GET':
        data = get_model_by_id(Order, pk)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )
    elif request.method == 'PUT':
        update_table(Order, pk, request.json)
        return app.response_class(
            response=json.dumps(['Данные успешно обновлены'], indent=4, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )
    elif request.method == 'DELETE':
        delete_data(Order, pk)
        return app.response_class(
            response=json.dumps(['Данные успешно удалены'], indent=4, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )


@app.route('/offers/<int:pk>', methods=['GET', 'PUT', 'DELETE'])
def get_offers_id(pk):
    if request.method == 'GET':
        data = get_model_by_id(Offer, pk)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )
    elif request.method == 'PUT':
        update_table(Offer, pk, request.json)
        return app.response_class(
            response=json.dumps(['Данные успешно обновлены'], indent=4, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )
    elif request.method == 'DELETE':
        delete_data(Offer, pk)
        return app.response_class(
            response=json.dumps(['Данные успешно удалены'], indent=4, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )


if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=8000)
