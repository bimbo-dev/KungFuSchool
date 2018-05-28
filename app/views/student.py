from flask import Blueprint, render_template, redirect, url_for, flash, jsonify
from ..forms import StudentForm, StudentBindingModel
from ..services.student_service import *


student = Blueprint('student', __name__)


@student.route('/student')
def index():
    students = get_all_students()
    return render_template('student/index.html', title='Students', items=students)


@student.route('/student/details/<studentid>')
def details(studentid):
    student = get_student_by_id(studentid)
    return render_template('student/details.html', title='Details', student=student)


@student.route('/student/create', methods=['GET', 'POST'])
@student.route('/student/edit/<studentid>', methods=['GET', 'POST'])
def save(studentid=None):
    title = 'Create'
    student_obj = StudentBindingModel()
    form = StudentForm()
    if studentid is not None:
        title = 'Edit'
        # fetch payment item
        student_obj = get_student_binding_model(studentid)
        form = StudentForm(obj=student_obj)
    if form.validate_on_submit():
        form.populate_obj(student_obj)
        try:
            save_student(student_obj)
            return redirect(url_for('student.index'))
        except:
            flash('An Error Occurred!')
    return render_template('student/create.html', title=title, form=form)


@student.route("/student/delete/<studentid>")
def delete(studentid):
    try:
        delete_student(studentid)
        success = True
    except:
        success = False

    data = {
        'success': success
    }
    resp = jsonify(data)
    return resp
