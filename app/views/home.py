from flask import Blueprint, render_template

home_route = Blueprint('home', __name__)



@home_route.route('/', methods=['GET'])
def home_index():
    user = {'username': 'Administrator'}
    return render_template('home/index.html', title='Home', user=user)
