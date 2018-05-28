from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, HiddenField
from wtforms.validators import DataRequired


class ClassForm(FlaskForm):
    id = HiddenField('Id')
    level_id = SelectField('Level',coerce=int, validators=[DataRequired()])
    class_day = SelectField('Class Day', validators=[DataRequired()])
    class_time = SelectField('Class Time', validators=[DataRequired()])
