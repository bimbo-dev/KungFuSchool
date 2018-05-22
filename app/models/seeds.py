from app import app, db
from ..models import User, PaymentItem
from werkzeug.security import generate_password_hash


@app.cli.command()
def seed_database():
    print('Seeding...')

    # Seeding the User Table
    admin_user, password = 'admin', 'Password123!'
    if db.session.query(User).scalar() is None:
        print('Seeding User table...')
        user = User(username=admin_user, password_hash=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()

    # Seeding Payment Item Table
    if db.session.query(PaymentItem).scalar() is None:
        print('Seeding Payment Item Table...')
        item1 = PaymentItem(description='School Fees', price=100)
        item2 = PaymentItem(description='School Uniform', price=25)
        db.session.add_all([item1, item2])
        db.session.commit()

    print('Done.')
