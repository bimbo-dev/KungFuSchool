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
    address = db.Column(db.Text)
    parents = db.relationship('Person', secondary=student_parents)
    is_deleted = db.Column(db.Boolean, default=False)


# Payment_Item Table
class PaymentItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(64), nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)


# Student_Payment Table
class StudentPayment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    payment_item_id = db.Column(db.Integer, db.ForeignKey('payment_item.id'), nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)


# Rank Table
class Rank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    belt_colour = db.Column(db.String(64), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)


# Student Rank Association Table
student_ranks = db.Table('student_ranks',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
    db.Column('rank_id', db.Integer, db.ForeignKey('rank.id'), primary_key=True),
    db.Column('date_attained', db.DateTime, nullable=False)
)


# Level Table
class Level(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(64), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)