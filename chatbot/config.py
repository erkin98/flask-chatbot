from __future__ import annotations

import os


def _get_env(name: str, default: str | None = None) -> str | None:
    value = os.environ.get(name)
    if value is None or value == "":
        return default
    return value


class Config:
    """
    Default Flask config.

    Values are environment-driven so secrets don't live in source control.
    """

    SECRET_KEY = _get_env("SECRET_KEY", "dev-secret-key")

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = _get_env("DATABASE_URL", "sqlite:///bot.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Twilio
    TWILIO_ACCOUNT_SID = _get_env("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = _get_env("TWILIO_AUTH_TOKEN")
    # Phone numbers can be plain E.164 or WhatsApp ("whatsapp:+...") depending on usage.
    TWILIO_PHONE_NUMBER = _get_env("TWILIO_PHONE_NUMBER")
