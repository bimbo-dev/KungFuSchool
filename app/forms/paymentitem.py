from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, FloatField
from wtforms.validators import DataRequired


class PaymentItemForm(FlaskForm):
    id = HiddenField('Id')
    description = StringField('Description', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
