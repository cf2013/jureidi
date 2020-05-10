from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC57faf4f1d528e9035cbdb02bf2408fef"
# Your Auth Token from twilio.com/console
auth_token  = "8ff0be458227f4fafd76bcc1c4284f9b"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="whatsapp:+524426778033", 
    from_="whatsapp:+14155238886",
    body="Hello from Python!")

print(message.sid)
