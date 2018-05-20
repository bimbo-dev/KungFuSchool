from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms import LoginForm

home = Blueprint('home', __name__, template_folder='templates')


@home.route('/', methods=['GET'])
def index():
    user = {'username': 'Administrator'}
    return render_template('home/index.html', title='Dashboard', user=user)


@home.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
       flash('Login requested for user {}, remember me = {}'.format(form.username.data, form.remember_me.data))
       return redirect(url_for('home.index'))
    return render_template('home/login.html', form=form)