from django.db import models


class Wallet(models.Model):
    cryptocurrencie = models.ForeignKey('cryptocurrencie.Cryptocurrencie', on_delete=models.PROTECT)
    user = models.ForeignKey('user.User', on_delete=models.PROTECT)

    amount = models.DecimalField(max_digits=15, decimal_places=15)

    def __str__(self):
        return f'{self.cryptocurrencie}'
