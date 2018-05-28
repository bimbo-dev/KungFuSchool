from app import db
from ..models import Student, Person
from ..forms import StudentBindingModel
from datetime import date


def get_all_students():
    return Student.query.filter_by(is_deleted=False).all()


def get_student_by_id(studentid):
    return Student.query.get(studentid)


def get_student_binding_model(studentid):
    student = Student.query.get(studentid)
    model = StudentBindingModel(
        id=student.id,
        last_name=student.person.last_name,
        first_name=student.person.first_name,
        other_names=student.person.other_names,
        phone_number=student.person.phone_number,
        email_address=student.person.email_address,
        date_of_birth=student.date_of_birth,
        address=student.address
    )
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
        db.session.add(new_student)
    db.session.commit()


def delete_student(studentid):
    if studentid is not None:
        student = Student.query.get(studentid)
        student.is_deleted = True
        db.session.commit()
