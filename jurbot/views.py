from django.http import HttpResponse
import requests
import twilio
import os
from twilio.rest import Client



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def bot(request):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    message = client.messages \
    .create(
    media_url=['https://images.unsplash.com/photo-1545093149-618ce3bcf49d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80'],
    from_='whatsapp:+14155238886',
    body="It's taco time!",
    to='whatsapp:+5214426778033'
    )
    print(message.sid)
