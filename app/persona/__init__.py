from flask import Blueprint

bp = Blueprint('persona', __name__)

from app.persona import routes
