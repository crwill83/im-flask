from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

# create our Models based off of our ERD
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(250), nullable=False)
    post = db.relationship('Post', backref='author', lazy=True)
    cart_item = db.relationship('Cart', backref='cart_user', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

# added tools, we'll see if we can replace Post
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(200), nullable=False, unique=False)
    item_model = db.Column(db.String(300), nullable=False, unique=False)
    item_serial = db.Column(db.String(300), nullable=False, unique=False)
    item_description = db.Column(db.String(500))
    item_image = db.Column(db.String(300))
    item_checkout_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    item_date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    cart_item = db.relationship('Cart', backref='cart_product', lazy=True)

    def __init__(self, item_name, item_model, item_serial, item_description, item_image, user_id):
        self.item_name = item_name
        self.item_model = item_model
        self.item_serial = item_serial
        self.item_description = item_description
        self.item_image = item_image
        self.user_id = user_id

    def to_dict(self):
        return {
            'id':self.id,
            'item_name':self.item_name,
            'item_model':self.item_model,
            'item_serial':self.item_serial,
            'item_description':self.item_description,
            'item_image':self.item_image,
            'item_checkout_date':self.item_checkout_date,
            'item_date_created':self.item_date_created,
            'user_id':self.user_id,
        }


# create database to store items added to a cart
# user_id   inventory_id
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False)

    def __init__(self, user_id, inventory_id):
        self.user_id = user_id
        self.inventory_id = inventory_id


class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_rented = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False)

    def __init__(self, user_id, inventory_id):
        self.user_id = user_id
        self.inventory_id = inventory_id


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, unique=False)
    image = db.Column(db.String(300))
    caption = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, image, caption, user_id):
        self.title = title
        self.image = image
        self.caption = caption
        self.user_id = user_id