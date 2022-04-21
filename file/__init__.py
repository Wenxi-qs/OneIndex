from flask import Blueprint

file_blue = Blueprint('file_blue', __name__, url_prefix='/file')
from file import views
