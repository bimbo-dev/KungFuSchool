from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# User Table
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# Person Table
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(64), nullable=False)
    first_name = db.Column(db.String(64), nullable=False)
    other_names = db.Column(db.String(64))
    phone_number = db.Column(db.String(32))
    email_address = db.Column(db.String(64))
    student = db.relationship('Student', backref='person', uselist=False)


# Student Parent Association Table
student_parents = db.Table('student_parents',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
    db.Column('person_id', db.Integer, db.ForeignKey('person.id'), primary_key=True)
)


# Student Table
class Student(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)
    date_of_birth = db.Column(db.Date, nullable=False)
    date_joined = db.Column(db.Date, nullable=False)
    address = db.Column(db.Text)
    parents = db.relationship('Person', secondary=student_parents)
    is_deleted = db.Column(db.Boolean, default=False)

    def full_name(self):
        return '{} {}'.format(self.person.first_name, self.person.last_name)

    def current_rank(self):
        if len(self.ranks) > 0:
            return (sorted(self.ranks, key=lambda rank: rank.date_attained, reverse=True))[0].rank.belt_colour or None
        else:
            return None


# Payment_Item Table
class PaymentItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(64), nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)

    def full_description(self):
        return '{} - ${:04.2f}'.format(self.description, self.price)


# Student Payment Association Table
class StudentPayment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    payment_item_id = db.Column(db.Integer, db.ForeignKey('payment_item.id'), nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)
    payment_item = db.relationship('PaymentItem')
    student = db.relationship('Student', backref='payments')


# Rank Table
class Rank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    belt_colour = db.Column(db.String(64), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)


# Student Rank Association
class StudentRank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    rank_id = db.Column(db.Integer, db.ForeignKey('rank.id'), nullable=False)
    date_attained = db.Column(db.DateTime, nullable=False)
    student = db.relationship('Student', backref='ranks')
    rank = db.relationship('Rank', backref='students')


# Level Table
class Level(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(64), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)
    classes = db.relationship('Class', backref='level', lazy=True)


class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'), nullable=False)
    class_day = db.Column(db.String(64), nullable=False)
    class_time = db.Column(db.String(32), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)

    def full_description(self):
        return '{} - {} {}'.format(self.level.description, self.class_day, self.class_time)


class ClassAttendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=False)
    date_attended = db.Column(db.Date, nullable=False)
    student = db.relationship('Student')
    class_obj = db.relationship('Class', backref='attendance')