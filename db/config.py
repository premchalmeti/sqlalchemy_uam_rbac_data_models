import os

DB_DIALECT = os.environ.get('DB_DIALECT')
DB_NAME = os.environ.get('DB_NAME')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = int(os.environ.get('DB_PORT'))

DB_PWD = os.environ.get('DB_PWD')
DB_USER = os.environ.get('DB_USER')

SQLA_URL = f'{DB_DIALECT}://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
