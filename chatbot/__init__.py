from __future__ import annotations

from flask import Flask

from chatbot.config import Config
from chatbot.extensions import db, migrate


def create_app(config_class: type[Config] = Config) -> Flask:
    """
    Flask application factory.

    Keeps side effects out of import-time so tooling (migrations/tests) behaves well.
    """

    app = Flask(
        __name__,
        static_folder="../frontend_bot/build/static",
        template_folder="../frontend_bot/build",
    )
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from chatbot.bot.routes import bots
    from chatbot.customers.routes import customers

    app.register_blueprint(bots)
    app.register_blueprint(customers)

    return app