from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, request
from ..forms import RankForm
from ..services.rank_service import *


rank = Blueprint('rank', __name__)


@rank.route('/rank')
def index():
    page = request.args.get('page', 1, type=int)
    ranks = get_all_ranks_by_page(page)
    next_url = url_for('rank.index', page=ranks.next_num) \
        if ranks.has_next else None
    prev_url = url_for('rank.index', page=ranks.prev_num) \
        if ranks.has_prev else None
    return render_template('rank/index.html', title='Ranks', items=ranks.items,
                           next_url=next_url, prev_url=prev_url)


@rank.route('/rank/create', methods=['GET', 'POST'])
@rank.route('/rank/edit/<rankid>', methods=['GET', 'POST'])
def save(rankid=None):
    title = 'Create'
    rank = Rank()
    form = RankForm()
    if rankid is not None:
        title = 'Edit'
        # fetch payment item
        rank = get_rank_by_id(rankid)
        form = RankForm(obj=rank)
    if form.validate_on_submit():
        form.populate_obj(rank)
        try:
            save_rank(rank)
            return redirect(url_for('rank.index'))
        except:
            flash('An Error Occurred!')
    return render_template('rank/create.html', title=title, form=form)


@rank.route("/rank/delete/<rankid>")
def delete(rankid):
    try:
        delete_rank(rankid)
        success = True
    except:
        success = False

    data = {
        'success': success
    }
    resp = jsonify(data)
    return resp
