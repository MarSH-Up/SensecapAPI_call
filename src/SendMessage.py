from twilio.rest import Client

import json

# Open the JSON file and load its contents
with open('src/credentials.json') as json_file:
    data = json.load(json_file)

# Get the values of account_sid and auth_token from the loaded JSON data


def sendWhatsApp(message_string):
    account_sid = data['account_sid']
    auth_token = data['auth_token']
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=message_string,
        to='whatsapp:+5212211683177'
    )

    print(message.sid)
