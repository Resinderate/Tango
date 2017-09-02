from django.db import models

from transactions.models import GameTransaction


class Spin(models.Model):
	transaction = models.OneToOneField(
		GameTransaction,
		on_delete=models.CASCADE,
		primary_key=True
	)
	stake = models.DecimalField(max_digits=10, decimal_places=2)
	won = models.BooleanField()
	game = models.CharField(max_length=50, choices=(,))
	roll = models.SmallIntegerField()
	# The list of numbers that you bet it would land on.
	# Would rather use an ArrayField, but need postgres for sure.
	# Should only be for logging purposes anyway, so just convert to string
	# for now.
	choices = models.CharField(max_length=255)
