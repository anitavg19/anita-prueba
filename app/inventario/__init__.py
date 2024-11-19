from flask import Blueprint

bp = Blueprint('inventario', __name__)

from app.inventario  import routes
