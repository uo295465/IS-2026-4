from flask import Blueprint

bienvenido = Blueprint('bienvenido', __name__)

from . import views