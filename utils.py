from models import *
from config import db
import json


def insert_data(model, input_data):
    """
    Функция сохранения получаемых данных в таблицы БД
    """
    for row in input_data:
        db.session.add(
            model(
                **row
            )
        )
    db.session.commit()


def init_db():
    """
    Ф-ция заполнения БД данными из json
    """
    db.drop_all()
    db.create_all()
    with open('data/users.json', 'r', encoding='utf-8') as file:
        insert_data(User, json.load(file))

    with open('data/order.json', 'r', encoding='utf-8') as file:
        insert_data(Order, json.load(file))

    with open('data/offers.json', 'r', encoding='utf-8') as file:
        insert_data(Offer, json.load(file))


def get_all(model):
    """
    Получение данных в зависимости от передаваемой модели
    """
    result = []
    for row in db.session.query(model).all():
        result.append(row.to_dict())
    return result


def get_model_by_id(model, pk):
    """
    Получение строки таблицы по pk
    """
    try:
        return db.session.query(model).get(pk).to_dict()
    except Exception:
        return {}


def update_table(model, pk, values):
    """
    Обновление данных строки таблицы
    """
    try:
        db.session.query(model).filter(model.id == pk).update(values)
        db.session.commit()
    except Exception:
        return 'Ошибка обновления данных'


def delete_data(model, pk):
    """
    Удаление строки
    """
    try:
        db.session.query(model).filter(model.id == pk).delete()
        db.session.commit()
    except Exception:
        return 'Ошибка удаления данных'
