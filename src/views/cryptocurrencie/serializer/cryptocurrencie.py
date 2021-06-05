from django.db import models
from rest_framework import serializers

from domain.cryptocurrencie.models import Cryptocurrencie


class CryptocurrencieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrencie
        fields = '__all__'


class CryptocurrencyOperationTypeChoices(models.TextChoices):
    BUY = 'BUY'
    SELL = 'SELL'


class CryptocurrencyOperationSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=15, decimal_places=10)
    type = serializers.ChoiceField(choices=CryptocurrencyOperationTypeChoices.choices)
