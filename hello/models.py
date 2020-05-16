from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class UsersBot(models.Model):
    phone = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)

