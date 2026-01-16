from __future__ import annotations

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Flask extensions are created once and initialized in the app factory.
db = SQLAlchemy()
migrate = Migrate()

