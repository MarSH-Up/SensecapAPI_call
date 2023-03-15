from twilio.rest import Client


def sendWhatsApp(message_string):
    account_sid = 'AC17d5d8f84a6367c55cb58d7148853294'
    auth_token = '3a993765a2c079938c6fc2cff5b2e448'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=message_string,
        to='whatsapp:+5212211683177'
    )

    print(message.sid)
