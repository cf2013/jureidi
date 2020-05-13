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
    from_='whatsapp:+14155238886',
    body=str(request.values['Body']),
    to='whatsapp:+5214426778033'
    )
    print(message.sid)
    # Return an HHTPResponse as Django expects a response from the view
    return HttpResponse(status=200)
