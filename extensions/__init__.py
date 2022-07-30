from flask import Flask

from extensions.CustomJSONEncoder import CustomJSONEncoder


def init_app(app: Flask) -> None:
    app.json_encoder = CustomJSONEncoder
