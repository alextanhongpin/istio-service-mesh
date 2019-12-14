FROM python:3.8-alpine3.10

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY main.py /app/main.py

WORKDIR /app

CMD ["python", "main.py"]
