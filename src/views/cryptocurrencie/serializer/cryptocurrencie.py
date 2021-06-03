from rest_framework import serializers

from domain.cryptocurrencie.models import Cryptocurrencie


class CryptocurrencieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrencie
        fields = '__all__'
