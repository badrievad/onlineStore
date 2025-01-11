import grpc
from flask import render_template

from . import warehouse_bp
from .protos import cars_catalog_pb2, cars_catalog_pb2_grpc


@warehouse_bp.route("/catalog", methods=["GET"])
def cars_catalog() -> str:
    # Устанавливаем соединение с gRPC-сервером
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = cars_catalog_pb2_grpc.CarsCatalogServiceStub(channel)
        response = stub.GetCarsCatalog(cars_catalog_pb2.Empty())

    # Преобразуем данные из gRPC-ответа в список словарей
    cars: list[dict] = [
        {
            "id": car.id,
            "name": car.name,
            "price": car.price,
            "image_url": car.image_url,
            "year": car.year,
            "color": car.color,
            "transmission": car.transmission,
            "old_price": car.old_price,
            "discount": car.discount,
            "drive_type": car.drive_type,
            "engine": car.engine,
            "fuel_type": car.fuel_type,
        }
        for car in response.cars
    ]

    # Передаем данные в шаблон
    return render_template("catalog.html", cars=cars)
