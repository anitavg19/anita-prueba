from flask import Blueprint

bp = Blueprint('bom', __name__, url_prefix='/bom')

from app.bom import routes
