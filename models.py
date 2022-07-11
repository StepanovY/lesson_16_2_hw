# Создаем модели для трех таблиц User, Order, Offer

from config import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    role = db.Column(db.String(200))
    phone = db.Column(db.String(100))

    def to_dict(self):
        """
        Преобразуем получаемые данные в словарь
        """
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone
        }


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    start_date = db.Column(db.String(200))
    end_date = db.Column(db.String(200))
    address = db.Column(db.String(200))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    customer = db.relationship('User', foreign_keys=[customer_id])
    executor = db.relationship('User', foreign_keys=[executor_id])

    def to_dict(self):
        """
        Преобразуем получаемые данные в словарь
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'address': self.address,
            'price': self.price
        }


class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    order = db.relationship('Order', foreign_keys=[order_id])
    executor = db.relationship('User', foreign_keys=[executor_id])

    def to_dict(self):
        """
        Преобразуем получаемые данные в словарь
        """
        return {
            'id': self.id,
            'order_id': self.order_id,
            'executor_id': self.executor_id,
        }
