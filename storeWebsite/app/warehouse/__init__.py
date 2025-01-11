from flask import Blueprint

warehouse_bp = Blueprint("warehouse", __name__)

from . import routes  # noqa F401
