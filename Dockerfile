FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install pdm

RUN pdm install

CMD ["python", "src/test_project/prime_functions.py", "1", "1"]
