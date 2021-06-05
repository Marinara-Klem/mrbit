import decimal

from django.db import models


class Wallet(models.Model):
    cryptocurrencie = models.ForeignKey('cryptocurrencie.Cryptocurrencie', on_delete=models.PROTECT)
    user = models.ForeignKey('user.User', on_delete=models.PROTECT)

    amount = models.DecimalField(max_digits=25, decimal_places=10, default=0)

    def __str__(self):
        return f'{self.cryptocurrencie}'

    @property
    def total_price_in_dollars(self):
        return self.cryptocurrencie.price_in_dollars * self.amount

    def has_enough_cryptocurrencies_for_sale(self, sale_quantity: decimal.Decimal):
        return self.amount >= sale_quantity

    def credit_cryptocurrencie(self, amount: decimal.Decimal):
        self.amount += amount

    def debit_cryptocurrencie(self, amount: decimal.Decimal):
        self.amount -= amount
