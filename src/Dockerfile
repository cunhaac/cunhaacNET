FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN apt-get clean \
    && apt-get -y update \
    && pip install --upgrade pip  \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

COPY . /app

EXPOSE 80

CMD flask run --host=0.0.0.0 --port=80

