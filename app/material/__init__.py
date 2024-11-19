from flask import Blueprint

bp = Blueprint('material', __name__, url_prefix='/material')

from app.material import routes
