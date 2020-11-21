FROM python:3.8

COPY requirements.txt /
RUN pip3 install -r / requirements.txt

COPY . /app
WORKDIR /app/cunhaacNET
# RUN export export 'HOME_DIR'=$(pwd)/:$'HOME_DIR'

EXPOSE 80

ENTRYPOINT [ "./gunicorn_starter.sh" ]
