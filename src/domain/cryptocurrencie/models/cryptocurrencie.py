from django.db import models


class Cryptocurrencie(models.Model):
    abbreviation = models.CharField(max_length=3)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.abbreviation} - {self.name}'
