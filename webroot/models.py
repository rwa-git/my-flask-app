from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    name = db.Column(db.String(150))
    notes = db.relationship('Note')


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.String(40), unique=True)
    item_desc = db.Column(db.String(80))
    item_desc_long = db.Column(db.String(200))
    stock = db.Column(db.Float)
    unit = db.Column(db.Integer)
    price_net = db.Column(db.Float)
    tax = db.Column(db.Float)


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pos = db.Column(db.Integer)
    item_id = db.Column(db.String(40), unique=True)
    qty = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

