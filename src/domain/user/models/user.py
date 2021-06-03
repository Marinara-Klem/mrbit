from django.db import models
from django.utils import timezone


class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=60)
    phone = models.CharField(max_length=20, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)

    cryptocurrencies = models.ManyToManyField('cryptocurrencie.Cryptocurrencie', through='cryptocurrencie.Wallet')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
