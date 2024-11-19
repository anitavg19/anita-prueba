from flask import Blueprint

bp = Blueprint('calendario_capacidad', __name__, url_prefix='/calendario_capacidad')

from app.calendario_capacidad import routes
