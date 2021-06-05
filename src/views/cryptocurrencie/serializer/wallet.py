from rest_framework import serializers

from domain.cryptocurrencie.models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    cryptocurrencie__abbreviation = serializers.ReadOnlyField(source='cryptocurrencie.abbreviation')
    cryptocurrencie__name = serializers.ReadOnlyField(source='cryptocurrencie.name')
    cryptocurrencie__price_in_dollars = serializers.DecimalField(source='cryptocurrencie.price_in_dollars', max_digits=15, decimal_places=2)
    total_price_in_dollars = serializers.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        model = Wallet
        fields = (
            'id', 'cryptocurrencie__abbreviation', 'cryptocurrencie__name', 'cryptocurrencie__price_in_dollars',
            'amount', 'total_price_in_dollars'
        )
