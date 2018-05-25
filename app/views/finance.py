from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, request
# from app.models import PaymentItem
from app.forms import PaymentItemForm
from ..services.payment_items_service import *

finance = Blueprint('finance', __name__)


@finance.route('/finance')
def index():
    page = request.args.get('page', 1, type=int)
    payment_items = get_all_payment_items_by_page(page)
    next_url = url_for('finance.index', page=payment_items.next_num) \
        if payment_items.has_next else None
    prev_url = url_for('finance.index', page=payment_items.prev_num) \
        if payment_items.has_prev else None
    return render_template('finance/index.html', title='Finance', items=payment_items.items,
                           next_url=next_url, prev_url=prev_url)


@finance.route('/finance/create', methods=['GET', 'POST'])
@finance.route('/finance/edit/<itemid>', methods=['GET', 'POST'])
def save(itemid=None):
    title = 'Create'
    item = PaymentItem()
    form = PaymentItemForm()
    if itemid is not None:
        title = 'Edit'
        # fetch payment item
        item = get_payment_item_by_id(itemid)
        form = PaymentItemForm(obj=item)
    if form.validate_on_submit():
        form.populate_obj(item)
        try:
            save_payment_item(item)
            return redirect(url_for('finance.index'))
        except:
            flash('An Error Occurred!')
    return render_template('finance/create.html', title=title, form=form)


@finance.route("/finance/delete/<itemid>")
def delete(itemid):
    # message = None
    success = False;
    try:
        delete_payment_item(itemid)
        message = "Item " + itemid + " deleted"
        success = True
    except:
        message = "Error"

    data = {
        'message': message,
        'success': success
    }
    resp = jsonify(data)
    return resp
