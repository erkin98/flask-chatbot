from __future__ import annotations

from flask import Blueprint, current_app, jsonify, render_template, request
from twilio.rest import Client

from chatbot.models import Customer

customers = Blueprint('customers', __name__)


def _get_twilio_client() -> Client | None:
    sid = current_app.config.get("TWILIO_ACCOUNT_SID")
    token = current_app.config.get("TWILIO_AUTH_TOKEN")
    if not sid or not token:
        current_app.logger.warning("Twilio credentials are not configured.")
        return None
    return Client(sid, token)


def _get_page_size() -> int:
    # Accept size from JSON body or query param, defaulting safely.
    size = None
    payload = request.get_json(silent=True) or {}
    if isinstance(payload, dict):
        size = payload.get("size")
    if size is None:
        size = request.args.get("size")
    try:
        size_int = int(size) if size is not None else 20
    except (TypeError, ValueError):
        size_int = 20
    return max(1, min(size_int, 200))


def get_msg(sender: str) -> list[tuple[str, str]]:
    client = _get_twilio_client()
    from_number = current_app.config.get("TWILIO_PHONE_NUMBER")
    if client is None or not from_number:
        current_app.logger.warning("Twilio phone number is not configured.")
        return []

    limit = _get_page_size()
    msgs: list[tuple[str, str]] = []

    messages = client.messages.list(from_=sender, to=from_number, limit=limit)
    responses = client.messages.list(from_=from_number, to=sender, limit=limit)

    for msg, reply in zip(messages, responses):
        message = client.messages(msg.sid).fetch()
        response = client.messages(reply.sid).fetch()
        msgs.append((message.body, response.body))

    return msgs


@customers.route('/', defaults={'path': ''})
@customers.route('/<path:path>')
def serve(path):

    return render_template('index.html')


@customers.route('/customers', methods=['GET', 'POST'])
def home():

    data = Customer.query.all()
    senders = [str(i) for i in data]
    return jsonify(data=senders)


@customers.route('/customers/<sender>', methods=['GET', 'POST'])
def go_sender(sender):
    return jsonify(data=get_msg(sender))
