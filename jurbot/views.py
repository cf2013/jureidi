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

DEFAULT_ERROR = "We are experimenting issues with the server, sorry!"

class Message:    
    whats = None
    body = None
    def __init__(self):
        self.whats = ""
        self.body = ""

    def isValid(self):
        if self.whats and self.body:
            return True
    
    def __str__(self):
        return "whats: %s"%self.whats +" "+ "question: %s"%self.body

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def botReply(ans, toReq):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

    #answer back
    client = Client(account_sid, auth_token)
    message = client.messages \
    .create(
        from_='whatsapp:+14155238886',
        body=ans,
        to='whatsapp:'+toReq
    )
    print(message.sid)
    # Return an HHTPResponse as Django expects a response from the view
    return HttpResponse(status=200)

def parseInput(request):
    msgCmp = Message()

    def semanticParse(unimsg):        
        args = unimsg.split("&")
        for argenc in args:
            try:
                (arg,val) = argenc.split("=")
            except:
                next
            if arg == "Body":
                msgCmp.body = val
            if arg == "From":
                msgCmp.whats = val.split(":") 
                msgCmp.whats = msgCmp.whats[1]
        
        if msgCmp.isValid():
            return True
        else:
            return False

    def doChat(q):
        ans = ""
        sq = str.upper(q)
        #modify
        if "HOLA" in sq:
            ans = "Hola! bienvenido soy un asistente de mesero, "\
            "En que te puedo servir?"
        elif "HI" in sq:
            ans = "Hello, spanish is prefered in Mex but, "\
            "How might I help you?"
        else:
            ans = "no entendi eso!, estoy en proceso de ser programado."
    
        return ans

    #ensure only utf-8
    body_unicode = request.body.decode('utf-8')
    #convert URL to unicode
    unq = unquote(body_unicode)
    answer = ""
    
    #check id client
    if unq:
        #ready to interact.
        #perform semantic parsing
        question = semanticParse(unq)
        if question:
            answer = doChat(msgCmp.body)
        else:
            answer = DEFAULT_ERROR
    else:
        answer = DEFAULT_ERROR

    return (answer, msgCmp)

@csrf_exempt
def bot(request):
    incomingMsg = Message()
    (ans, incomingMsg) = parseInput(request)    
    botReply(ans, incomingMsg.whats)
    
    # Return an HHTPResponse as Django expects a response from the view
    return HttpResponse(status=200)

