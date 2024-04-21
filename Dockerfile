FROM python:3.12.1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn --bind 0.0.0.0:8888 run:app