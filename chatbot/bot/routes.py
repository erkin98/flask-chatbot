# from chatbot.models import Customer,Message, Response
from flask import request, Blueprint
from twilio.twiml.messaging_response import MessagingResponse
from chatbot import db
from chatbot.models import Customer
import datetime


bots = Blueprint('bots', __name__)


@bots.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body').lower()
    sender_num = request.values.get('From').lower()
    date = request.values.get('MessageSid')
    print(date)
    if not (bool(Customer.query.filter_by(sender=sender_num).first())):
        # db.drop_all()
        # db.create_all()
        send_id = Customer(sender=sender_num)
        db.session.add(send_id)
        db.session.commit()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    countries = {k.lower(): v.lower() for k, v in countries.items()}

    if 'salam' in incoming_msg:
        quote = '\'Salam.Siz chatbot ilə əlaqədəsiniz.Sizə necə kömək edə bilərik?\''

        msg.body(quote)
        responded = True

    # our_msg = Response(response = quote)
    # db.session.add(our_msg)
    # o_id = Response(our_id = 'Azeri Student')
    # db.session.add(o_id)
    # db.session.commit()
    print(datetime.datetime.now())
    return str(resp)
