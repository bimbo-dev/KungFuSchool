from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(64), nullable=False)
    first_name = db.Column(db.String(64), nullable=False)
    other_names = db.Column(db.String(64))
    phone_number = db.Column(db.String(32))
    email_address = db.Column(db.String(64))
    student = db.relationship('Student', backref='person', uselist=False)


student_parents = db.Table('student_parents',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
    db.Column('person_id', db.Integer, db.ForeignKey('person.id'), primary_key=True)
)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_of_birth = db.Column(db.Date, nullable=False)
    address = db.Column(db.Text)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    person = db.relationship('Person', backref='student')
    parents = db.relationship('Person', secondary=student_parents, backref='student')


