import os
from flask import Flask


app = Flask(__name__)
APP_ENV = os.environ.get('APP_ENV')
app.config.from_object(f"project.config.{APP_ENV}Config")

