from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

# Items model
class Item(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    code = db.Column(db.String(50))
    name = db.Column(db.String(300))
    price = db.Column(db.String(50))
    category = db.Column(db.String(50))
    
    def __init__(self, code, name, price, category):
        self.code = code
        self.name = name
        self.price = price
        self.category = category

    def serialize(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "price": self.price,
            "category": self.category
        }