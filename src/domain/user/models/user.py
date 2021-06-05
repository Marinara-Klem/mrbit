import decimal

from django.db import models
from django.utils import timezone


class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=60)
    phone = models.CharField(max_length=20, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    balance = models.DecimalField(decimal_places=2, max_digits=15, default=0)

    cryptocurrencies = models.ManyToManyField('cryptocurrencie.Cryptocurrencie', through='cryptocurrencie.Wallet')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def has_balance_for_purchase(self, purchase_amount: decimal.Decimal):
        return self.balance >= purchase_amount

    def debit_balance(self, amount: decimal.Decimal):
        if self.has_balance_for_purchase(purchase_amount=amount):
            self.balance -= decimal.Decimal(amount)
            return True

        return False

    def credit_balance(self, amount: decimal.Decimal):
        self.balance += decimal.Decimal(amount)

    @property
    def wallet_value_in_dollars(self):
        return sum(wallet.total_price_in_dollars for wallet in self.wallet_set.all())
