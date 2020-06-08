from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import os

app = Flask(__name__)
#os.environ.get('SECRET_KEY')
#os.environ.get('DATABASE_URL')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)
share = Share(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'users.signin'
login_manager.login_message_category = 'info'

from finalyear.users.routes import users
from finalyear.main.routes import main
from finalyear.admin.routes import admin
from finalyear.errors.handlers import errors

app.register_blueprint(users)
app.register_blueprint(main)
app.register_blueprint(admin)
app.register_blueprint(errors)