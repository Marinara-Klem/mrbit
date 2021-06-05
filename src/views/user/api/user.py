from rest_framework import viewsets, decorators, response, status, pagination

from domain.user.models import User
from views.user.serializer import UserSerializer, UserBalanceCreateSerializer, UserRetrieveSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'balances':
            return UserBalanceCreateSerializer
        elif self.action == 'retrieve':
            return UserRetrieveSerializer
        return super().get_serializer_class()

    @decorators.action(methods=['post'], detail=True, url_path='balances')
    def balances(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        amount = serializer.validated_data.get('amount')

        user = self.get_object()
        user.credit_balance(amount=amount)
        user.save()

        return response.Response({f'${amount} incluido(s) no saldo com sucesso'}, status=status.HTTP_201_CREATED)
