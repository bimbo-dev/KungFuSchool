from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, HiddenField, SelectMultipleField
from wtforms.validators import DataRequired


class ClassForm(FlaskForm):
    id = HiddenField('Id')
    level_id = SelectField('Level', coerce=int, validators=[DataRequired()])
    class_day = SelectField('Class Day', validators=[DataRequired()])
    class_time = SelectField('Class Time', validators=[DataRequired()])


class ClassAttendanceForm(FlaskForm):
    id = HiddenField('Id')
    class_id = HiddenField('Class Id')
    student_id = SelectMultipleField('Student', coerce=int, validators=[DataRequired()])
