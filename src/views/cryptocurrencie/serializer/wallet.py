from rest_framework import serializers

from domain.cryptocurrencie.models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    cryptocurrencie__abbreviation = serializers.ReadOnlyField(source='cryptocurrencie.abbreviation')
    cryptocurrencie__name = serializers.ReadOnlyField(source='cryptocurrencie.name')

    class Meta:
        model = Wallet
        fields = ('id', 'cryptocurrencie__abbreviation', 'cryptocurrencie__name', 'amount')


# class WalletSerializerBuySell(serializers.ModelSerializer):
#     cryptocurrencie__abbreviation = serializers.ReadOnlyField(source='cryptocurrencie.abbreviation')
#     cryptocurrencie__name = serializers.ReadOnlyField(source='cryptocurrencie.name')
#
#     class Meta:
#         model = Wallet
#         fields = ('id', 'cryptocurrencie__abbreviation', 'cryptocurrencie__name', 'amount')
