from app import app, db
from app.models import PaymentItem, StudentPayment
from datetime import datetime, timedelta


def get_all_payments():
    return StudentPayment.query.all()


def get_all_payments_in_range(begin, end):
    enddate = datetime.strptime(end, '%Y-%m-%d') + timedelta(days=1)
    end = enddate.strftime('%Y-%m-%d')
    return StudentPayment.query.filter(StudentPayment.payment_date.between(begin, end))


def get_all_payment_items():
    return PaymentItem.query.filter_by(is_deleted=False).all()


def get_all_payment_items_by_page(page):
    return PaymentItem.query.order_by(PaymentItem.description) \
        .filter_by(is_deleted=False) \
        .paginate(page, app.config['PAGE_SIZE'], False)


def get_payment_item_by_id(id):
    return PaymentItem.query.get(id);


def save_payment_item(paymentitem):
    if paymentitem.id != '':
        item = PaymentItem.query.get(paymentitem.id)
        if item is not None:
            item.description = paymentitem.description
            item.price = paymentitem.price
    else:
        paymentitem.id = None
        paymentitem.is_deleted = False
        db.session.add(paymentitem)
    db.session.commit()


def delete_payment_item(paymentitemid):
    if paymentitemid is not None:
        payment = PaymentItem.query.get(paymentitemid)
        payment.is_deleted = True
        db.session.commit()