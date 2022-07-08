

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
        body= f'LIVA batchjob have reported errors on critical batchjobs. Take immediate action to handle this \n************\n{alertMessage}',
        from_=keys.twilio_number,
        to=keys.sravan_number
    )

    message = client.messages.create(
        body= f'LIVA batchjob have reported errors on critical batchjobs. Take immediate action to handle this \n************\n{alertMessage}',
        from_=keys.twilio_number,
        to=keys.mahesh_number
    )


    print(message.body)
else:
    print("There are no Critical jobs found")


