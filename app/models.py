from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


class Profile(models.Model):
    user_profile=models.ForeignKey(User,on_delete=models.CASCADE)
    btc=models.IntegerField(default=5)
    usd=models.IntegerField(default=100000)
    initial_balance=models.IntegerField()

class Order(models.Model):
    profile=models.ForeignKey(User,on_delete=models.CASCADE)
    datetime=models.DateTimeField(default=timezone.now())
    price=models.FloatField()
    quantity=models.FloatField()

class BuyOffer(Order):
    pass
