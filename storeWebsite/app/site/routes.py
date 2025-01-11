from flask import (
    redirect,
    url_for,
)
from werkzeug.wrappers import Response

from . import web_bp


@web_bp.route("/", methods=["GET"])
def index() -> Response:
    return redirect(url_for("warehouse.cars_catalog"))
