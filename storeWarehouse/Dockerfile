# Используем базовый образ Python 3.12
FROM python:3.12-slim

# Устанавливаем конкретную рабочую директорию
WORKDIR /storeWarehouse_service

# Копируем файлы проекта
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Указываем порт для gRPC сервера
EXPOSE 50051

# Запуск gRPC сервера через catalog.py
CMD ["python", "catalog.py"]
