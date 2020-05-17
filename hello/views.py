from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import UsersBot
import requests

# Create your views here.
def index(request):
    return HttpResponse('200')


def db(request):

    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()

    #ask name if not number in usersBot
    userId = UsersBot()
    userId.save()

    return render(request, "db.html", {"greetings": greetings})
