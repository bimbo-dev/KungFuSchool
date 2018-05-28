from flask import Blueprint, render_template, redirect, url_for, flash, jsonify
from ..forms import ClassForm
from ..services.class_service import *
from ..services.level_service import get_all_levels


classes = Blueprint('classes', __name__)


@classes.route('/classes')
def index():
    all_classes = get_all_classes()
    return render_template('classes/index.html', title='Classes', items=all_classes)


@classes.route('/classes/create', methods=['GET', 'POST'])
@classes.route('/classes/edit/<classid>', methods=['GET', 'POST'])
def save(classid=None):
    title = 'Create'
    class_obj = Class()
    form = ClassForm()
    form.level_id.choices = [(level.id, level.description) for level in get_all_levels()]
    form.class_day.choices = [(d, d) for d in days_of_the_week()]
    form.class_time.choices = [(t, t) for t in hours_of_the_day()]
    if form.validate_on_submit():
        form.populate_obj(class_obj)
        try:
            save_class(class_obj)
            return redirect(url_for('classes.index'))
        except:
            flash('An Error Occurred!')
    if classid is not None:
        title = 'Edit'
        # fetch payment item
        class_obj = get_class_by_id(classid)
        form.id.data = class_obj.id
        form.level_id.data = class_obj.level_id
        form.class_day.data = class_obj.class_day
        form.class_time.data = class_obj.class_time
    return render_template('classes/create.html', title=title, form=form)


@classes.route("/classes/delete/<classid>")
def delete(classid):
    try:
        delete_class(classid)
        success = True
    except:
        success = False

    data = {
        'success': success
    }
    resp = jsonify(data)
    return resp


@classes.route("/classes/vacant/<day>/<time>/<id>")
def is_vacant(day, time, id):
    class_obj = get_class_by_day_time(day, time)
    vacant = True
    if class_obj is not None:
        if class_obj.id != int(id):
            vacant = False
    data = {
        'vacant': vacant
    }
    return jsonify(data)


def days_of_the_week():
    return ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def hours_of_the_day():
    hours = []
    start_hour = 9
    for i in range(0, 13):
        hour = start_hour + i
        if hour > 12:
            hours.append("%d pm" % (hour - 12))
        else:
            merdn = 'am'
            if hour == 12: merdn = 'pm'
            hours.append("%d %s" % (hour, merdn))
    return hours

