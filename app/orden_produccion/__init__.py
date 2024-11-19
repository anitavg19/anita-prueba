from flask import Blueprint

bp = Blueprint('orden_produccion', __name__, url_prefix='/orden_produccion')

from app.orden_produccion import routes
