from flask import Flask

from commands.import_us_stocks_from_finviz import import_us_stocks_from_finviz


def init_app(app: Flask) -> None:
    app.cli.add_command(import_us_stocks_from_finviz)