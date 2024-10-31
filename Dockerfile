FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    unixodbc \
    unixodbc-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV FLASK_APP=apirest.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
