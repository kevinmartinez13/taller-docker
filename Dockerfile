FROM python:3.8-slim-buster

WORKDIR /app

RUN pip install --no-cache-dir flask

COPY app.py .

EXPOSE 5050

CMD ["python", "app.py"]