from flask import Blueprint, render_template, redirect, url_for, flash, jsonify
from ..forms import StudentForm, StudentBindingModel, PersonForm, StudentRankForm, StudentPaymentForm
from ..services.student_service import *
from ..services.rank_service import get_all_ranks
from ..services.finance_service import get_all_payment_items


student = Blueprint('student', __name__)


@student.route('/student')
def index():
    students = get_all_students()
    return render_template('student/index.html', title='Students', items=students)


@student.route('/student/details/<studentid>')
def details(studentid):
    student = get_student_by_id(studentid)
    return render_template('student/details.html', title='Student Details', student=student)


@student.route('/student/create', methods=['GET', 'POST'])
@student.route('/student/edit/<studentid>', methods=['GET', 'POST'])
def save(studentid=None):
    title = 'Create'
    back_url = url_for('student.index')
    student_obj = StudentBindingModel()
    form = StudentForm()
    if studentid is not None:
        title = 'Edit'
        back_url = url_for('student.details', studentid=studentid)
        student_obj = get_student_binding_model(studentid)
        form = StudentForm(obj=student_obj)
    if form.validate_on_submit():
        form.populate_obj(student_obj)
        try:
            save_student(student_obj)
            return redirect(back_url)
        except:
            flash('An Error Occurred!')
    return render_template('student/create.html', title=title, form=form, back_url=back_url)


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


@student.route("/student/<studentid>/addparent", methods=['GET', 'POST'])
@student.route("/student/<studentid>/editparent/<parentid>", methods=['GET', 'POST'])
def add_parent(studentid, parentid=None):
    title = 'Create'
    person = Person()
    form = PersonForm()
    if form.validate_on_submit():
        form.populate_obj(person)
        try:
            save_parent(person, studentid)
            return redirect(url_for('student.details', studentid=studentid))
        except:
            flash('An Error Occurred!')
    if parentid is not None:
        title = 'Edit'
        person = get_parent_by_id(parentid)
        form = PersonForm(obj=person)
    return render_template('student/parent.html', title=title, form=form, studentId=studentid)


@student.route("/student/<studentid>/deleteparent/<parentid>")
def remove_parent(studentid, parentid):
    try:
        remove_parent(parentid, studentid)
        success = True
    except:
        success = False

    data = {
        'success': success
    }
    resp = jsonify(data)
    return resp


@student.route('/student/updaterank/<studentid>', methods=['GET', 'POST'])
def update_rank(studentid):
    title = 'Update Rank'
    student_rank = StudentRank()
    d_student = get_student_by_id(studentid)
    form = StudentRankForm()
    form.rank_id.choices = [(rank.id, rank.belt_colour) for rank in get_all_ranks()
                            if rank.id not in [r.rank_id for r in d_student.ranks]]
    if form.validate_on_submit():
        form.populate_obj(student_rank)
        try:
            add_student_rank(student_rank)
            return redirect(url_for('student.update_rank', studentid=studentid))
        except:
            flash('An Error Occurred!')
    form.student_id.data = studentid
    return render_template('student/updaterank.html', title=title, form=form, student=d_student)


@student.route('/student/removerank/<id>')
def remove_student_rank(id):
    try:
        remove_rank(id)
        success = True
    except:
        success = False

    return jsonify({'success': success})


@student.route('/student/payment/<studentid>', methods=['GET', 'POST'])
def make_payment(studentid):
    title = 'Payments';
    student_payment = StudentPayment()
    d_student = get_student_by_id(studentid)
    form = StudentPaymentForm()
    form.payment_item_id.choices = [(item.id, item.full_description()) for item in get_all_payment_items()]
    if form.validate_on_submit():
        form.populate_obj(student_payment)
        try:
            add_student_payment(student_payment)
            return redirect(url_for('student.make_payment', studentid=studentid))
        except:
            flash('An Error Occured!')
    form.student_id.data = studentid
    return render_template('student/payments.html', title=title, form=form, student=d_student)


@student.route('/student/removepayment/<id>')
def remove_student_payment(id):
    try:
        remove_payment(id)
        success = True
    except:
        success = False

    return jsonify({'success': success})