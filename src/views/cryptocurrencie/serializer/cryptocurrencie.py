from django.db import models
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from domain.cryptocurrencie.models import Cryptocurrencie


class CryptocurrencieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrencie
        fields = '__all__'


class CryptocurrencyOperationTypeChoices(models.TextChoices):
    BUY = 'BUY'
    SELL = 'SELL'


class ValidateAmount:
    @staticmethod
    def validate_amount(amount):
        if not amount > 0:
            msg = 'A quantidade de criptomoedas não pode ser menor ou igual a zero'
            raise ValidationError(msg)

        return amount


class UserCryptocurrentiesCreateSerializer(ValidateAmount, serializers.Serializer):
    amount = serializers.DecimalField(max_digits=25, decimal_places=10)
    cryptocurrency_id = serializers.IntegerField(min_value=0)


class CryptocurrencyOperationSerializer(ValidateAmount, serializers.Serializer):
    user_id = serializers.IntegerField(min_value=0)
    amount = serializers.DecimalField(max_digits=25, decimal_places=10)
    type = serializers.ChoiceField(choices=CryptocurrencyOperationTypeChoices.choices)
