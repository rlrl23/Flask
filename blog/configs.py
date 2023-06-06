import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv('DEBUG')
#TESTING = os.getenv('TESTING')
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SECRET_KEY = os.getenv('SECRET_KEY')
WTF_CSRF_ENABLED = True
FLASK_ADMIN_SWATCH = 'cosmo'
OPENAPI_URL_PREFIX = '/api/swagger'
OPENAPI_SWAGGER_UI_PATH = '/'
OPENAPI_SWAGGER_UI_VERSION = '3.22.0'
