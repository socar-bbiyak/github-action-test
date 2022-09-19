FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install

CMD uvicorn --host=0.0.0.0 --port 8000 main:app