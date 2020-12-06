import os

DB_USER = os.environ.get('MYSQL_USER')
DB_PASS = os.environ.get('MYSQL_PASSWORD')
DB_HOST = os.environ.get('MYSQL_HOST')
DB_PORT = os.environ.get('MYSQL_PORT')
DB_NAME = os.environ.get('MYSQL_DATABASE')

MAIL_SERVER = os.environ.get('MAIL_SERVER')
MAIL_PORT = os.environ.get('MAIL_PORT')
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

SECRET_KEY = os.environ.get('SECRET_KEY')
