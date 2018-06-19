from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired


class RankForm(FlaskForm):
    id = HiddenField('Id')
    belt_colour = StringField('Belt Colour', validators=[DataRequired()])
