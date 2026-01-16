# from chatbot.models import Customer,Message, Response
from __future__ import annotations

from flask import Blueprint, current_app, request
from twilio.twiml.messaging_response import MessagingResponse
from chatbot.extensions import db
from chatbot.models import Customer
import datetime


bots = Blueprint('bots', __name__)


@bots.route('/bot', methods=['POST'])
def bot():
    incoming_msg = (request.values.get("Body") or "").strip().lower()
    sender_num = (request.values.get("From") or "").strip().lower()

    if sender_num and Customer.query.filter_by(sender=sender_num).first() is None:
        db.session.add(Customer(sender=sender_num))
        db.session.commit()

    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if 'salam' in incoming_msg:
        quote = '\'Salam.Siz chatbot ilə əlaqədəsiniz.Sizə necə kömək edə bilərik?\''

        msg.body(quote)
        responded = True

    # our_msg = Response(response = quote)
    # db.session.add(our_msg)
    # o_id = Response(our_id = 'Azeri Student')
    # db.session.add(o_id)
    # db.session.commit()
    if not responded:
        # Keep a polite default reply instead of returning an empty TwiML message.
        msg.body("Mesajınızı aldıq. Zəhmət olmasa sualınızı dəqiqləşdirin.")

    current_app.logger.info("Bot message processed at %s", datetime.datetime.now().isoformat())
    return str(resp)
