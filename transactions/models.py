"""
Maybe these don't need to be split up at all?

They could just have 1 to 1's with other stuff.
	But then you would have to check what other stuff they have.

I kinda like this version better.
"""

from django.db import models

from wallets.models import Wallet


class Transaction(models.Model):
	"""Something that brings the balance of a wallet up or down.

	These transactions should be reflected in the wallets they point to as they are created.
	Do it in the init or something.
	"""
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	wallet = models.ForeignKey(Wallet)

	class Meta:
		abstract = True

class UserTransaction(Transaction):
	"""A transaction where the source of the amount is the user's external money source.

	A deposit to the account, a withdrawl from the account
	"""
	# Bank account?, some sort of money source.
	pass


class StaffTransaction(Transaction):
	"""A transaction where the source of the amount is from the platform.

	From promotions, docking amounts from users..
	"""
	# Could have a FK to some sort of elaborated reason here.
	reason = models.CharField(max_length=512)


class GameTransaction(Transaction):
	"""A transaction where the source of the amount is from a game.

	A spin that loses/wins the player some money..
	"""
	stake = models.DecimalField(max_digits=10, decimal_places=2)
	won = models.BooleanField()
	# Could record the odds, in case it's not fixed.