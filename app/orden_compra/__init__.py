from flask import Blueprint

bp = Blueprint('orden_compra', __name__, url_prefix='/orden_compra')

from app.orden_compra import routes
