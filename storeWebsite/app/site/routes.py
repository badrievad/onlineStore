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
    cars: list[dict] = [
        {"id": 1, "name": "Audi RSQ8", "price": 25000000, "image_url": "/static/images/audi_rsq8.jpg", "year": 2023, "color": "черный", "transmission": "АКПП"},
        {"id": 2, "name": "Geely Coolray", "price": 3000000, "image_url": "/static/images/geely_coolray.jpg", "year": 2024, "color": "серый", "transmission": "АКПП"},
        {"id": 3, "name": "Haval Jolion", "price": 2700000, "image_url": "/static/images/haval_jolion.jpg", "year": 2024, "color": "белый", "transmission": "АКПП"},
    ]
    return render_template("catalog.html", cars=cars)
