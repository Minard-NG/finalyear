from finalyear import db, login_manager
from finalyear.utils import unique_id
from flask_login import UserMixin
from datetime import datetime as dt

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	uuid = db.Column(db.String(10), nullable=False, unique=True)
	fullname = db.Column(db.String(30), nullable=False)
	email = db.Column(db.String(50), unique=True, nullable=False)
	phone = db.Column(db.String(15), default='')
	password = db.Column(db.String(120), nullable=False)
	user_status = db.Column(db.String(10), nullable=False, default='student')
	
	def __repr__(self):
		return f"User('{self.fullname}','{self.password}','{self.email}','{self.phone}'')"
