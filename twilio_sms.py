

from twilio.rest import Client
import keys
import os

client = Client(keys.account_sid, keys.auth_token)
filepath_critical_result = os.getcwd() + "/critical_result.txt"

alert = open('critical_result.txt', 'r')
alertMessage = alert.read()
alert.close()
# if os.path.getsize(filepath_critical_result) != 0 and os.stat(filepath_critical_result).st_size != 0:
if os.path.getsize(filepath_critical_result) != 0: 

    message = client.messages.create(
        body= f'Here is the list of the critical job that has come under the error \n************\n{alertMessage}',
        from_=keys.twilio_number,
        to=keys.sravan_number
    )
    print(message.body)
else:
    print("There are no Critical jobs found")


