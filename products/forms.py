from wtforms import Form, StringField, TextAreaField, IntegerField


class ProductForm(Form):
    name = StringField('Name')
    price = IntegerField('Price')
    amount = IntegerField('Amount')
    comment = TextAreaField('Comment')

