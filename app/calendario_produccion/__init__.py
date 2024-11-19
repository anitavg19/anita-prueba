from flask import Blueprint

bp = Blueprint('calendario_produccion', __name__, url_prefix='/calendario_produccion')

from app.calendario_produccion import routes
