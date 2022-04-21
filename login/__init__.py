from flask import Blueprint

login_blue = Blueprint('login_blue', __name__, url_prefix='/login')
from login import views
