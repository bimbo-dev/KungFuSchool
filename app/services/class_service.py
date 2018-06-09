from app import db
from ..models import Class, ClassAttendance
from datetime import date


def get_all_classes():
    return Class.query.filter_by(is_deleted=False).all()


def get_class_by_id(classid):
    return Class.query.get(classid)


def save_class(class_obj):
    if class_obj.id != '':
        class_obj_old = Class.query.get(class_obj.id)
        if class_obj_old is not None:
            class_obj_old.level_id = class_obj.level_id
            class_obj_old.class_day = class_obj.class_day
            class_obj_old.class_time = class_obj.class_time
    else:
        class_obj.id = None
        db.session.add(class_obj)
    db.session.commit()


def delete_class(classid):
    if classid is not None:
        class_obj = Class.query.get(classid)
        class_obj.is_deleted = True
        db.session.commit()


def get_class_by_day_time(day, time):
    return Class.query.filter_by(is_deleted=False, class_day=day, class_time=time).first()


def add_attendance(form):
    today = date.today()
    students = form.student_id.data
    attendance = [ClassAttendance(student_id=st, class_id=form.class_id.data, date_attended=today) for st in students]
    db.session.add_all(attendance)
    db.session.commit()


def remove_attandance(id):
    attendance = ClassAttendance.query.get(id)
    db.session.delete(attendance)
    db.session.commit()