from flask import Blueprint

bp = Blueprint('centro_trabajo', __name__, url_prefix='/centro_trabajo')

from app.centro_trabajo import routes
