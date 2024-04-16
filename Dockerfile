FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y wkhtmltopdf

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn --bind 0.0.0.0:8888 run:app