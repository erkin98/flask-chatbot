from chatbot.models import Customer
from flask import Blueprint, jsonify, render_template, request
from twilio.rest import Client
from chatbot import db

customers = Blueprint('customers', __name__)
account_sid = 'xxx'
auth_token = 'xxx'
client = Client(account_sid, auth_token)


def get_msg(sender):
    msgs = []
    data = request.get_json()['size']
    messages = client.messages.list(
        from_=sender, to='whatsapp:+xxx', limit=data)
    responses = client.messages.list(
        from_='whatsapp:+xxx', to=sender, limit=data)
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
