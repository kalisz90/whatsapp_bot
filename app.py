from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/sms', methods=['POST'])
def sms_reply():
    msg = request.form.get('Body')

    resp = MessagingResponse()
    resp.message('Twoja wiadomość: {}'.format(msg))

    return str(resp)


if __name__=='__main__':

    app.run(debug=True)
