from django.contrib.auth.models import User
from django.db import models

class Wallet(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	balance = models.DecimalField(max_digits=10, decimal_places=2)
	play_money = models.BooleanField(default=True)
	currency = models.CharField(max_length=50) # Add choices here eventually.
