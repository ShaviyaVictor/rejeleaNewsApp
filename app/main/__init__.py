from flask import Blueprint
from pip import main
main = Blueprint('main', __name__)
from . import views, error
