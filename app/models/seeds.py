from app import app, db
from ..models import User, PaymentItem, Rank, Level
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

    # Seeding Rank Table
    if db.session.query(Rank).scalar() is None:
        print('Seeding Rank Table')
        db.session.add_all([
            Rank(id=1, belt_colour='White'),
            Rank(id=2, belt_colour='Yellow'),
            Rank(id=3, belt_colour='Half Green'),
            Rank(id=4, belt_colour='Green'),
            Rank(id=5, belt_colour='Half Blue'),
            Rank(id=6, belt_colour='Blue'),
            Rank(id=7, belt_colour='Half Red'),
            Rank(id=8, belt_colour='Red'),
            Rank(id=9, belt_colour='Half Black'),
            Rank(id=10, belt_colour='Black')
        ])
        db.session.commit()

    # Seeding Level Table
    if db.session.query(Level).scalar() is None:
        print('Seeding Level Table')
        db.session.add_all([
            Level(id=1, description='Beginner'),
            Level(id=2, description='Intermediate'),
            Level(id=3, description='Advanced')
        ])
        db.session.commit()

    print('Done.')
