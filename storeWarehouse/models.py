from protos import cars_catalog_pb2, cars_catalog_pb2_grpc


class CarsCatalogService(cars_catalog_pb2_grpc.CarsCatalogServiceServicer):
    def GetCarsCatalog(self, request, context) -> cars_catalog_pb2.CarsCatalogResponse:
        cars: list[dict] = [
            {
                "id": 1,
                "name": "Audi RS Q8",
                "price": "25 000 000",
                "image_url": "/static/images/audi_rsq8.jpg",
                "year": 2023,
                "color": "черный",
                "transmission": "АКПП",
                "old_price": "30 000 000",
                "discount": "5 000 000",
                "drive_type": "4WD",
                "engine": 4.0,
                "fuel_type": "бензин",
            },
            {
                "id": 2,
                "name": "Geely Coolray",
                "price": "3 000 000",
                "image_url": "/static/images/geely_coolray.jpg",
                "year": 2024,
                "color": "серый",
                "transmission": "АКПП",
                "old_price": "3 500 000",
                "discount": "500 000",
                "drive_type": "передний",
                "engine": 1.5,
                "fuel_type": "бензин",
            },
            {
                "id": 3,
                "name": "Haval Jolion",
                "price": "2 700 000",
                "image_url": "/static/images/haval_jolion.jpg",
                "year": 2024,
                "color": "белый",
                "transmission": "АКПП",
                "old_price": "3 000 000",
                "discount": "300 000",
                "drive_type": "передний",
                "engine": 1.5,
                "fuel_type": "бензин",
            },
            {
                "id": 4,
                "name": "Mercedes-Benz G-Класс 350 d",
                "price": "20 500 000",
                "image_url": "/static/images/mercedes.jpg",
                "year": 2021,
                "color": "белый",
                "transmission": "АКПП",
                "old_price": "23 000 000",
                "discount": "2 500 000",
                "drive_type": "4WD",
                "engine": 2.9,
                "fuel_type": "дизель",
            },
            {
                "id": 5,
                "name": "BMW X5 M Competition",
                "price": "26 000 000",
                "image_url": "/static/images/bmw.jpg",
                "year": 2024,
                "color": "серый",
                "transmission": "АКПП",
                "old_price": "30 000 000",
                "discount": "4 000 000",
                "drive_type": "4WD",
                "engine": 4.4,
                "fuel_type": "бензин",
            },
        ]

        # Преобразуем данные в формат CarsCatalogResponse
        car_objects = [
            cars_catalog_pb2.Car(
                id=car["id"],
                name=car["name"],
                price=car["price"],
                image_url=car["image_url"],
                year=car["year"],
                color=car["color"],
                transmission=car["transmission"],
                old_price=car["old_price"],
                discount=car["discount"],
                drive_type=car["drive_type"],
                engine=car["engine"],
                fuel_type=car["fuel_type"],
            )
            for car in cars
        ]

        return cars_catalog_pb2.CarsCatalogResponse(cars=car_objects)
