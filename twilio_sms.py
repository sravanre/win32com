

from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)

message = client.messages.create(
    body="new message from the Twilio to sravan kumar ",
    from_=keys.twilio_number,
    to=keys.mahesh_number
)


print(message.body)