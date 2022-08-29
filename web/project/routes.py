import json

from flask import jsonify

from . import app


def media_status_loader(file_name: str):
    """Media file loader based on request name"""
    try:
        with open(f'{app.config.get("MEDIA_FOLDER")}/{file_name}.json', 'r') as f:
            return json.load(f), 200
    except FileNotFoundError:
        return {"error": "Not Found"}, 404


@app.route("/")
@app.route("/<file_name>")
def index(file_name=None):
    output, status = media_status_loader(file_name if file_name else 'index')
    return jsonify(output), status
