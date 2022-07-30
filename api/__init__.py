from flask import Flask
from api.symbol import bp as symbol_blueprint
from api.symbol_stats import bp as symbol_stats_blueprint


def init_app(app: Flask) -> None:
    app.register_blueprint(symbol_blueprint)
    app.register_blueprint(symbol_stats_blueprint)