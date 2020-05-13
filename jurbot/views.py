from django.http import HttpResponse
from django.http import HttpRequest
import requests
import twilio
import os
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def bot(request):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    body_unicode = request.body.decode('utf-8')
    from urllib.parse import unquote
    unq = unquote(body_unicode)
    #check id client
    if request:
        ans=str(unq)
    else:
        ans='source'
    #answer back
    client = Client(account_sid, auth_token)
    message = client.messages \
    .create(
    from_='whatsapp:+14155238886',
    body=ans,
    to='whatsapp:+5214426778033'
    )
    print(message.sid)
    # Return an HHTPResponse as Django expects a response from the view
    return HttpResponse(status=200)

