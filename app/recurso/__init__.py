from flask import Blueprint

bp = Blueprint('recurso', __name__, url_prefix='/recurso')

from app.recurso import routes
