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
        {"id": 1, "name": "Audi RS Q8", "price": "25 000 000", "image_url": "/static/images/audi_rsq8.jpg", "year": 2023, "color": "черный", "transmission": "АКПП", "old_price": "30 000 000", "discount": "5 000 000", "drive_type": "4WD", "engine": 4.0, "fuel_type": "бензин"},
        {"id": 2, "name": "Geely Coolray", "price": "3 000 000", "image_url": "/static/images/geely_coolray.jpg", "year": 2024, "color": "серый", "transmission": "АКПП", "old_price": "3 500 000", "discount": "500 000", "drive_type": "передний", "engine": 1.5, "fuel_type": "бензин"},
        {"id": 3, "name": "Haval Jolion", "price": "2 700 000", "image_url": "/static/images/haval_jolion.jpg", "year": 2024, "color": "белый", "transmission": "АКПП", "old_price": "3 000 000", "discount": "300 000", "drive_type": "передний", "engine": 1.5, "fuel_type": "бензин"},
        {"id": 4, "name": "Mercedes-Benz G-Класс 350 d", "price": "20 500 000", "image_url": "/static/images/mercedes.jpg", "year": 2021, "color": "белый", "transmission": "АКПП", "old_price": "23 000 000", "discount": "2 500 000", "drive_type": "4WD", "engine": 2.9, "fuel_type": "дизель"},
        {"id": 5, "name": "BMW X5 M Competition", "price": "26 000 000", "image_url": "/static/images/bmw.jpg", "year": 2024, "color": "серый", "transmission": "АКПП", "old_price": "30 000 000", "discount": "4 000 000", "drive_type": "4WD", "engine": 4.4, "fuel_type": "бензин"},
    ]
    return render_template("catalog.html", cars=cars)
