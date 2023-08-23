FROM python:3.11

WORKDIR /kurs_8

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .