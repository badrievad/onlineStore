from flask import (
    redirect,
    render_template,
    url_for,
)
from werkzeug.wrappers import Response

from . import web_bp


@web_bp.route("/", methods=["GET"])
def index() -> Response:
    return redirect(url_for("web.cars_catalog"))


@web_bp.route("/catalog", methods=["GET"])
def cars_catalog() -> str:
    return render_template("catalog.html")
