import decimal

from django.db import models

from domain.cryptocurrencie import utils


class Cryptocurrencie(models.Model):
    abbreviation = models.CharField(max_length=10)
    name = models.CharField(max_length=30)

    @property
    def price_in_dollars(self):
        return utils.cryptocurrencies_for_dollars(cryptocurrency_abbreviation=self.abbreviation)

    def transaction_amount(self, amount: decimal.Decimal):
        if self.price_in_dollars:
            return self.price_in_dollars * amount

    def __str__(self):
        return f'{self.abbreviation}-{self.name}'
