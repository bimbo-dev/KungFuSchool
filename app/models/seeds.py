from app import app, db
from ..models import User, PaymentItem, Rank, Level, Class, Student, Person, StudentRank
from werkzeug.security import generate_password_hash
from datetime import datetime, date


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

    # Seeding Class Table
    if db.session.query(Class).scalar() is None:
        print('Seeding Classes Table')
        db.session.add_all([
            Class(level_id=1, class_day='Monday', class_time='10 am'),
            Class(level_id=2, class_day='Tuesday', class_time='3 pm'),
            Class(level_id=3, class_day='Wednesday', class_time='8 pm')
        ])
        db.session.commit()

    # Seeding Student Table
    if db.session.query(Student).scalar() is None:
        print('Seeding Student Table')
        student_one = Student(person=Person(last_name='Doe', first_name='John', other_names='',
                            phone_number='5552338533', email_address='john@mail.com'),
                    date_of_birth=datetime.strptime('1999-04-04', '%Y-%m-%d').date(), date_joined=date.today())
        student_two = Student(person=Person(last_name='Essien', first_name='Mark', other_names='',
                            phone_number='5552234553', email_address='mark@mail.com'),
                    date_of_birth=datetime.strptime('1989-12-24', '%Y-%m-%d').date(), date_joined=date.today())
        student_one.ranks.append(StudentRank(rank_id=1, date_attained=date.today()))
        student_two.ranks.append(StudentRank(rank_id=1, date_attained=date.today()))
        db.session.add_all([student_one, student_two])
        db.session.commit()

    print('Done.')
