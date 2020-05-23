from django.http import HttpResponse
from django.http import HttpRequest
import requests
import twilio
import os
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
import json
import psycopg2
from .models import Clients
from urllib.parse import unquote
from urllib.parse import urlencode

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def botReply(ans):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

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

def parseInput(request):
    body_unicode = request.body.decode('utf-8')
    unq = unquote(body_unicode)
    
    pfrom = ""
    #check id client
    if request:
        ans=str(unq)
        pfrom = str(ans)
    else:
        ans='source'
    return pfrom

@csrf_exempt
def bot(request):
    ans = parseInput(request)    
    botReply(ans)
    
    # Return an HHTPResponse as Django expects a response from the view
    return HttpResponse(status=200)