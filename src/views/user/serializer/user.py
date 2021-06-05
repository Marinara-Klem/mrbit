from rest_framework import serializers

from domain.user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'phone')


class UserBalanceCreateSerializer(serializers.Serializer):
    amount = serializers.DecimalField(help_text='amount in dollars(USD)', max_digits=15, decimal_places=2)

