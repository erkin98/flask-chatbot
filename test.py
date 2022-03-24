from twilio.rest import Client

account_sid = 'xxx'
auth_token = 'xxx'
client = Client(account_sid, auth_token)

messages = client.messages.list(to='whatsapp:+xxx')

x = [record.from_ for record in messages]
print(set(x))
