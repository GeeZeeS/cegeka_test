import os
from pathlib import Path


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    APPLICATION_COMMON_TITLE = 'CegekaTest'
    SECRET_KEY = '9OLWexND4osdfd55f86ydu5d3s4stasd3j4K4iuorpO'
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/project/static"
    TEMPLATES_FOLDER = f"{os.getenv('APP_FOLDER')}/project/templates"
    MEDIA_FOLDER = f"{os.getenv('APP_FOLDER')}/project/media"

    JSON_SORT_KEYS = False


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True


class FinalConfig(Config):
    DEBUG = False
