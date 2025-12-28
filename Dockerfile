FROM python:3.12-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /code

# Устанавливаем системные зависимости для работы с Postgres
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Копируем файл с зависимостями
COPY requirements.txt .

# Устанавливаем Python-пакеты
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь остальной код проекта
COPY . .
