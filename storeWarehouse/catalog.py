from concurrent import futures

import grpc

from logger import logging
from models import CarsCatalogService
from protos import cars_catalog_pb2_grpc


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cars_catalog_pb2_grpc.add_CarsCatalogServiceServicer_to_server(
        CarsCatalogService(), server
    )
    server.add_insecure_port("[::]:50051")
    logging.info("gRPC сервер запущен на порту 50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
