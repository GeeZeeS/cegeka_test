from flask import jsonify
from . import app
from .utils import media_status_loader


@app.route("/")
@app.route("/<file_name>")
def index(file_name=None):
    output, status = media_status_loader(file_name if file_name else 'index')
    return jsonify(output), status
