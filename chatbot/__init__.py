from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from chatbot.config import Config


db = SQLAlchemy()
migrate = Migrate(db)



def create_app(config_class = Config):
    app = Flask(__name__,static_folder="../frontend_bot/build/static",template_folder="../frontend_bot/build")
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app)

    from chatbot.bot.routes import bots
    from chatbot.customers.routes import customers

    app.register_blueprint(bots)
    app.register_blueprint(customers)

    return app