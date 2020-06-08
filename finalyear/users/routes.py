from flask import Blueprint, render_template, url_for, flash, redirect, request
from finalyear import app, db
from datetime import datetime as dt
from finalyear.utils import unique_id
from finalyear.users.forms import UserRegForm, UserLogForm, PasswordChangeForm
from passlib.hash import sha256_crypt as sha256
from flask_login import login_user, current_user, logout_user, login_required
from finalyear.models import User

users = Blueprint('users', __name__)

error_message = 'Error on our side, try again later!'

@users.route('/signup', methods=['GET', 'POST'])
def signup():
	if current_user.is_authenticated:
		return redirect(url_for('users.userdashboard'))
	form = UserRegForm()
	if form.validate_on_submit():
		uuid = unique_id()
		hashed_password = sha256.encrypt(str(form.password.data))
		try:
			user = User(fullname=form.fullname.data,email=form.email.data,password=hashed_password, uuid=uuid)
			db.session.add(user)
			db.session.commit()
			flash('Your account has been created successfully.', 'success')
			return redirect(url_for('users.signin'))
		except Exception as e:
			flash(error_message, 'warning')
			return redirect(url_for('users.signup'))	
	return render_template('signup.html', form=form, title='Register')

@users.route('/signin', methods=['GET','POST'])
def signin():
	if current_user.is_authenticated:
		return redirect(url_for('users.userdashboard'))
	form = UserLogForm()
	if form.validate_on_submit():
		#change email login to reg number login
		user = User.query.filter_by(email=form.email.data).first()
		if user and sha256.verify(form.password.data, user.password):
			login_user(user)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('users.userdashboard'))
		else:
			#change email to reg number
			flash('Login Unsuccessful. Email or password invalid', 'danger')
	return render_template('signin.html', form=form, title='Login')

@users.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('users.signin'))

@users.route('/userdashboard')
@login_required
def userdashboard():
	return render_template('userdashboard.html', title='Dashboard', shared=len(picked_ads), posted=len(shared_ads), posts=posts, refer_balance=refer_balance)

@users.route('/changepassword', methods=['POST'])
@login_required
def changepassword():
	pform = PasswordChangeForm()
	if pform.validate_on_submit():
		try:
			if sha256.verify(pform.oldpassword.data, current_user.password):
				current_user.password = sha256.encrypt(str(pform.newpassword.data))
				db.session.commit()
				flash('Password changed successfully', 'success')
			else:
				flash('Your password does not match', 'info')
		except Exception as e:
			flash(error_message, 'warning')
		finally:
			return redirect(url_for('users.usersettings'))
	else:	
		flash('Your password does not match', 'info')
		return redirect(url_for('users.usersettings'))
