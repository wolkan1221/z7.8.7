# Используем официальный образ Python на базе Alpine для меньшего размера
FROM python:3.9-alpine

# Устанавливаем зависимости и копируем приложение в один слой
RUN pip install requests && mkdir /app
COPY app.py /app/app.py

# Указываем рабочую директорию
WORKDIR /app

# Запускаем приложение при старте контейнера
ENTRYPOINT ["python", "app.py"]
