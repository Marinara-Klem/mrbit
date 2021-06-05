from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from domain.user.models import User
from views.cryptocurrencie.serializer import WalletSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class UserRetrieveSerializer(UserSerializer):
    wallet_value_in_dollars = serializers.DecimalField(max_digits=15, decimal_places=2)
    wallet = serializers.SerializerMethodField()

    @staticmethod
    @swagger_serializer_method(serializer_or_field=WalletSerializer)
    def get_wallet(obj):
        return WalletSerializer(obj.wallet_set.all(), many=True).data

    class Meta(UserSerializer.Meta):
        model = User
        fields = (*UserSerializer.Meta.fields, 'email', 'phone', 'wallet_value_in_dollars', 'wallet')


class UserBalanceCreateSerializer(serializers.Serializer):
    amount = serializers.DecimalField(help_text='amount in dollars(USD)', max_digits=15, decimal_places=2)

