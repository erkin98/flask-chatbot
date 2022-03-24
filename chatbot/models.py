from chatbot import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String)
    # messages = db.relationship('Message',backref = 'sender',lazy = True)

    def __repr__(self):
        return f'{self.sender}'

# class Message(db.Model):
#     id = db.Column(db.Integer,primary_key = True)
#     message = db.Column(db.String)

#     customer_id  = db.Column(db.Integer,db.ForeignKey('customer.id'))

#     def __repr__(self):
#         return self.message

# class Response(db.Model):
#     id = db.Column(db.Integer,primary_key = True)
#     response = db.Column(db.String)
#     def __repr__(self):
#         return f"('{self.response}')"
