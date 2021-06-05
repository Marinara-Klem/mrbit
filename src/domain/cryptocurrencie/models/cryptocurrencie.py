import decimal

from django.db import models


class Cryptocurrencie(models.Model):
    abbreviation = models.CharField(max_length=3)
    name = models.CharField(max_length=30)

    @property
    def value(self):
        return decimal.Decimal(1)

    def transaction_amount(self, amount: decimal.Decimal):
        if self.value:
            return self.value * amount

    def __str__(self):
        return f'{self.abbreviation}-{self.name}'
