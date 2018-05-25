from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, request
from ..forms import LevelForm
from ..services.level_service import *


level = Blueprint('level', __name__)


@level.route('/level')
def index():
    page = request.args.get('page', 1, type=int)
    levels = get_all_levels_by_page(page)
    next_url = url_for('level.index', page=levels.next_num) \
        if levels.has_next else None
    prev_url = url_for('level.index', page=levels.prev_num) \
        if levels.has_prev else None
    return render_template('level/index.html', title='Levels', items=levels.items,
                           next_url=next_url, prev_url=prev_url)


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
