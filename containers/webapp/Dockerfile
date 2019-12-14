FROM python:3.8-alpine3.10

COPY requirements.txt /
RUN pip install -r requirements.txt

ARG VERSION

COPY ${VERSION}.py /app/main.py

WORKDIR /app

# NOTE: This is not a production-ready Dockerfile.
CMD ["python", "main.py"]
