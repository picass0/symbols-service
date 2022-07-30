from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://symbols:secret@db/symbols'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    import commands
    commands.init_app(app)

    import api
    api.init_app(app)

    import extensions
    extensions.init_app(app)

    return app
