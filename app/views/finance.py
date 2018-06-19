from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, request
# from app.models import PaymentItem
from app.forms import PaymentItemForm
from ..services.finance_service import *

finance = Blueprint('finance', __name__)


@finance.route('/finance')
def index():
    # begin = request.args.get('begin', )
    begin = request.args.get('begin', None)
    end = request.args.get('end', None)
    if begin is not None and end is not None:
        payments = get_all_payments_in_range(begin, end)
    else:
        payments = get_all_payments()
    range = {'Begin': begin or '', 'End': end or ''}
    return render_template('finance/index.html', title='Finance', items=payments, range=range)


@finance.route('/finance/items')
def paymentitems():
    payment_items = get_all_payment_items()
    return render_template('finance/paymentitem.html', title='Payment Item', items=payment_items)


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
            return redirect(url_for('finance.paymentitems'))
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
