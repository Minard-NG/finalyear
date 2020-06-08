from flask import Blueprint, render_template, url_for, flash, redirect, request
from ihu import app, db
from flask_login import current_user

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():

	return render_template('index.html', title='Home')
