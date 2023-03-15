from twilio.rest import Client


def sendWhatsApp(message_string):
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=message_string,
        to='whatsapp:+5212211683177'
    )

    print(message.sid)
