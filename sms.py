from twilio.rest import Client
account_sid = "AC1cba51c4dd136***************************bdba2f196f8d"
auth_token = "56e07990e4098c0******************************2d6f8a01ce13"
client = Client(account_sid, auth_token)

message = client.messages.create( body="security alert face detecd", from_='+142437***050', to='+91****542408')

print(message.sid)
