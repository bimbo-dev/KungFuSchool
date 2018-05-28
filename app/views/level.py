from flask import Blueprint, render_template, redirect, url_for, flash, jsonify
from ..forms import LevelForm
from ..services.level_service import *


level = Blueprint('level', __name__)


@level.route('/level')
def index():
    levels = get_all_levels()
    return render_template('level/index.html', title='Levels', items=levels)


@level.route('/level/create', methods=['GET', 'POST'])
@level.route('/level/edit/<levelid>', methods=['GET', 'POST'])
def save(levelid=None):
    title = 'Create'
    level_obj = Level()
    form = LevelForm()
    if levelid is not None:
        title = 'Edit'
        # fetch payment item
        level_obj = get_level_by_id(levelid)
        form = LevelForm(obj=level_obj)
    if form.validate_on_submit():
        form.populate_obj(level_obj)
        try:
            save_level(level_obj)
            return redirect(url_for('level.index'))
        except:
            flash('An Error Occurred!')
    return render_template('level/create.html', title=title, form=form)


@level.route("/level/delete/<levelid>")
def delete(levelid):
    try:
        delete_level(levelid)
        success = True
    except:
        success = False

    data = {
        'success': success
    }
    resp = jsonify(data)
    return resp
