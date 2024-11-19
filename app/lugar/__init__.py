from flask import Blueprint

bp = Blueprint('lugar', __name__)

from app.lugar import routes
