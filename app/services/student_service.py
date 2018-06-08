from app import db
from ..models import Student, Person, StudentRank, Rank, StudentPayment
from ..forms import StudentBindingModel
from datetime import date, datetime


def get_all_students():
    return Student.query.filter_by(is_deleted=False).all()


def get_student_by_id(studentid):
    return Student.query.get(studentid)


def get_student_binding_model(studentid):
    student = Student.query.get(studentid)
    model = StudentBindingModel()
    model.id = student.id
    model.last_name = student.person.last_name
    model.first_name = student.person.first_name
    model.other_names = student.person.other_names
    model.phone_number = student.person.phone_number
    model.email_address = student.person.email_address
    model.date_of_birth = student.date_of_birth
    model.address = student.address
    return model


def save_student(student):
    if student.id != '':
        student_obj = Student.query.get(student.id);
        if student_obj is not None:
            student_obj.person.last_name = student.last_name
            student_obj.person.first_name = student.first_name
            student_obj.person.other_names = student.other_names
            student_obj.person.phone_number = student.phone_number
            student_obj.person.email_address = student.email_address
            student_obj.date_of_birth = student.date_of_birth
            student_obj.address = student.address
    else:
        new_student = Student(
            person=Person(
                last_name=student.last_name,
                first_name=student.first_name,
                other_names=student.other_names,
                phone_number=student.phone_number,
                email_address=student.email_address
            ),
            date_of_birth=student.date_of_birth,
            address=student.address,
            date_joined=date.today()
        )
        rank = Rank.query.filter_by(belt_colour='White').first()
        if rank is not None:
            new_student.ranks.append(StudentRank(rank=rank, date_attained=date.today()))
        db.session.add(new_student)
    db.session.commit()


def delete_student(studentid):
    if studentid is not None:
        student = Student.query.get(studentid)
        student.is_deleted = True
        db.session.commit()


def get_parent_by_id(personid):
    return Person.query.get(personid)


def save_parent(person, studentid=None):
    if person.id != '':
        person_obj = Person.query.get(person.id);
        if person_obj is not None:
            person_obj.last_name = person.last_name
            person_obj.first_name = person.first_name
            person_obj.other_names = person.other_names
            person_obj.phone_number = person.phone_number
            person_obj.email_address = person.email_address
    else:
        parent = Person(
            last_name=person.last_name,
            first_name=person.first_name,
            other_names=person.other_names,
            phone_number=person.phone_number,
            email_address=person.email_address
        )
        student = Student.query.get(studentid)
        student.parents.append(parent)
    db.session.commit()


def remove_parent(parentid, studentid):
    student = Student.query.get(studentid)
    parent = Person.query.get(parentid)
    if student is not None:
        student.parents.delete(parent)
        db.session.commit()


def add_student_rank(student_rank):
    student_rank.id = None
    student_rank.date_attained = datetime.now()
    db.session.add(student_rank)
    db.session.commit()


def remove_rank(student_rank_id):
    student_rank = StudentRank.query.get(student_rank_id)
    db.session.delete(student_rank)
    db.session.commit()


def add_student_payment(student_payment):
    student_payment.id = None
    student_payment.payment_date = datetime.now()
    db.session.add(student_payment)
    db.session.commit()


def remove_payment(student_payment_id):
    student_payment = StudentPayment.query.get(student_payment_id)
    db.session.delete(student_payment)
    db.session.commit()