from django.db import models
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from domain.cryptocurrencie import utils
from domain.cryptocurrencie.models import Cryptocurrencie


class CryptocurrencieSerializer(serializers.ModelSerializer):
    @staticmethod
    def validate_abbreviation(abbreviation):
        abbreviation = abbreviation.upper()
        if not utils.valid_cryptocurrency_abbreviation(abbreviation=abbreviation):
            msg = 'A abreviação não esta relacionada a nenhuma criptomoeda conhecida'
            raise ValidationError(msg)

        return abbreviation

    price_in_dollars = serializers.DecimalField(max_digits=15, decimal_places=2, required=False, read_only=True)

    class Meta:
        model = Cryptocurrencie
        fields = ('id', 'abbreviation', 'name', 'price_in_dollars')


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
    def validate_user_id(self, user_id):
        request = self.context.get('request')
        view = self.context.get('view')

        if request and view and request.data.get('user_id') == int(view.kwargs.get('user_pk')):
            msg = 'Um usuario não pode ser o vendedor e comprador na mesma operação'
            raise ValidationError(msg)

        return user_id

    user_id = serializers.IntegerField(min_value=0)
    amount = serializers.DecimalField(max_digits=25, decimal_places=10)
    type = serializers.ChoiceField(choices=CryptocurrencyOperationTypeChoices.choices)
