from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "A*****************************"
# Your Auth Token from twilio.com/console
auth_token  = "*****************************"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hi!",
    to="********", 
    from_="*********")

print(message.sid)
