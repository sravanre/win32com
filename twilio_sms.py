

from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)

alert content

message = client.messages.create(
    body= {open('inprogress_file_dupsremoved.txt','r').read()},
    from_=keys.twilio_number,
    to=keys.sravan_number
)


print(message.body)

