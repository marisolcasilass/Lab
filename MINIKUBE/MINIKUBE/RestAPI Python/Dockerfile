FROM python:3.9-alpine

RUN apk add --no-cache python3-dev \
    && pip install --upgrade pip


WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3","src/API.py"]