from django.http import HttpResponse
import requests
import twilio
import os
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def bot(request):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    #check id client
    


    #answer back
    client = Client(account_sid, auth_token)
    message = client.messages \
    .create(
    media_url=['https://images.unsplash.com/photo-1545093149-618ce3bcf49d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80'],
    from_='whatsapp:+14155238886',
    body=str(request),
    to='whatsapp:+5214426778033'
    )
    print(message.sid)
    # Return an HHTPResponse as Django expects a response from the view
    return HttpResponse(status=200)
