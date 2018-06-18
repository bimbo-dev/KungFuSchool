from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User

home = Blueprint('home', __name__)


@home.route('/')
@home.route('/index')
@login_required
def index():
    return render_template('home/index.html', title='Welcome to KungFu Master')


@home.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('home.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home.index'))
    return render_template('home/login.html', form=form)


@home.route('/logout')
def logout():
    logout_user();
    return redirect(url_for('home.login'))