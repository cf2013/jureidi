from django.db import models

# Create your models here.
class Clients(models.Model):
    whats = models.CharField(max_length = 15)

class Client(models.Model):
    whats = models.CharField(max_length = 15)
    name = models.CharField(max_length = 30)

class Menu(models.Model):
    item = models.CharField(max_length = 30)
    desc = models.CharField(max_length = 50)
    price = models.IntegerField()
    discount = models.IntegerField()
    pic = models.CharField(max_length = 100)
    

class Bill(models.Model):
    id_client = models.IntegerField()
    id_menu = models.IntegerField()
    menu_price = models.IntegerField()
    menu_disc = models.IntegerField()
    status = models.CharField(max_length = 1)
    total  = models.IntegerField()
    