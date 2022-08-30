import json
from . import app


def media_status_loader(file_name: str):
    """Media file loader based on request name"""
    try:
        with open(f'{app.config.get("MEDIA_FOLDER")}/{file_name}.json', 'r') as f:
            return json.load(f), 200
    except FileNotFoundError:
        return {"error": "Not Found"}, 404
