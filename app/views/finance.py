from flask import Blueprint, render_template
from app.models import PaymentItem

finance = Blueprint('finance', __name__)


@finance.route('/finance')
def index():
    payment_items = []
    return render_template('finance/index.html', title='Finance', items=payment_items)

