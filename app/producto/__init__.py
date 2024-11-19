from flask import Blueprint

bp = Blueprint('producto', __name__, url_prefix='/producto')

from app.producto import routes
