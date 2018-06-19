from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired


class LevelForm(FlaskForm):
    id = HiddenField('Id')
    description = StringField('Description', validators=[DataRequired()])
