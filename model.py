from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    comment = db.Column(db.Text)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'<id:{self.id} name:{self.name} price:{self.price} amount:{self.amount}>'


