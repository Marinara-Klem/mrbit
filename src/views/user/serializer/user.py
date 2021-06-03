from rest_framework import serializers

from domain.user.models import User
from views.cryptocurrencie.serializer.wallet import WalletSerializer


class UserSerializer(serializers.ModelSerializer):
    wallet = serializers.SerializerMethodField()

    def get_wallet(self, obj):
        return WalletSerializer(obj.wallet_set.all(), many=True).data

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'wallet')
