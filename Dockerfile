FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install pdm

RUN pdm install

CMD ["python3", "src/test_project/main.py"]
