from app import db
import re


def slug_create(str):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', str)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    comment = db.Column(db.Text)
    slug = db.Column(db.String, unique=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.name:
            self.slug = slug_create(self.name)

    def __repr__(self):
        return f'<id {self.id} name {self.name} price {self.price} amount {self.amount}>'


