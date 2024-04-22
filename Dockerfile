FROM python:3.12.1

RUN apt-get update

RUN apt-get install -y wkhtmltopdf

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn --bind 0.0.0.0:8888 run:app