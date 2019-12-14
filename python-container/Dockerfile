FROM python:3.8-alpine3.10

# Install cython, and remove it.
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
 && pip install cython \
 && pip install gunicorn \
 && apk del .build-deps

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY main.py /app/main.py

WORKDIR /app

CMD ["gunicorn", "-b", "0.0.0.0", "-w 4", "main:app"]
