from twilio.rest import Client
import config

client = Client(config.account_sid, config.auth_token)


message = client.messages \
                .create(
                     body="welcome to the world of PYTHON",
                     from_='+13615414573',
                     to='+918960092084'
                 )


print(message.sid)