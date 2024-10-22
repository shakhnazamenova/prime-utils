FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install pdm

RUN pdm install

CMD ["pytest", "tests"]

