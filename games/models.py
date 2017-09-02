from django.db import models

from games.constants import GAME_CHOICES
from transactions.models import GameTransaction


class Spin(models.Model):
	transaction = models.OneToOneField(
		GameTransaction,
		on_delete=models.CASCADE,
		primary_key=True
	)
	stake = models.DecimalField(max_digits=10, decimal_places=2)
	won = models.BooleanField()
	# This is the same as the transaction amount
	outcome = models.DecimalField(max_digits=10, decimal_places=2)
	# Need to add logic for a single game, and add as a choice.
	# Maybe this is a bit pre-mature, but anyway.
	game = models.CharField(max_length=50, choices=GAME_CHOICES)
	# The list of numbers that you bet it would land on.
	# Would rather use an ArrayField, but need postgres for sure.
	# Should only be for logging purposes anyway, so just convert to string
	# for now.
	choices = models.CharField(max_length=255)
	roll = models.SmallIntegerField()

	def __init__(self, *args, wallet=None, **kwargs):
		super().__init__(*args, **kwargs)
		# Go do the game logic.
		# Will decide: won, outcome, roll.
		transaction = GameTransaction(wallet=wallet, amount=outcome)


# post(game="BAML", stake=5.00, wallet=12, numbers=[1, 2, 3, 4, 5])

# spin = Spin(game=BAML, stake=5, numbers=[1, 2, 3], wallet=12)
# Boom done.
# The spin is in charge of making the GameTransaction.

# Unlike the other transactions, like User or Staff ones, where these are their
# own events.
