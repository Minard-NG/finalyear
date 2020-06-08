from flask import Blueprint, render_template, url_for, flash, redirect, request, abort
from ihu import app, db
from ihu.utils import unique_id
from flask_login import login_user, current_user, login_required

admin = Blueprint('admin', __name__)
