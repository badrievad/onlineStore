# Используем базовый образ Python 3.12
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем проект
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Делаем run.sh исполняемым
RUN chmod +x run.sh

# Указываем порт для Flask
EXPOSE 5000

# Запуск через run.sh
CMD ["./run.sh"]
