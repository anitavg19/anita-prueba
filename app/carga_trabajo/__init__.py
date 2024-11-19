from flask import Blueprint

bp = Blueprint('carga_trabajo', __name__, url_prefix='/carga_trabajo')

from app.carga_trabajo import routes
