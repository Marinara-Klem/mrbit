from django.shortcuts import get_object_or_404
from rest_framework import viewsets, decorators, response, status, mixins
from rest_framework.exceptions import ValidationError

from domain.cryptocurrencie.models import Cryptocurrencie
from domain.user.models import User
from services import CryptocurrencyOperationService
from views.cryptocurrencie.serializer import CryptocurrencieSerializer, CryptocurrencyOperationSerializer
from views.cryptocurrencie.serializer.cryptocurrencie import CryptocurrencyOperationTypeChoices, \
    UserCryptocurrentiesCreateSerializer


class CryptocurrencieViewSet(viewsets.ModelViewSet):
    serializer_class = CryptocurrencieSerializer
    queryset = Cryptocurrencie.objects.all()


class CryptocurrencyOperationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CryptocurrencyOperationSerializer
    queryset = Cryptocurrencie.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            return UserCryptocurrentiesCreateSerializer
        return super().get_serializer_class()

    def create(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_object_or_404(User, pk=kwargs.get('user_pk'))
        cryptocurrencie = get_object_or_404(Cryptocurrencie, pk=serializer.validated_data.get('cryptocurrency_id'))

        cryptocurrency_user, _ = user.wallet_set.get_or_create(
            cryptocurrencie=cryptocurrencie
        )

        amount = serializer.validated_data.get('amount')
        cryptocurrency_user.credit_cryptocurrencie(amount=amount)
        cryptocurrency_user.save()

        msg = {f'{cryptocurrencie} incluidos na carteira com sucesso'}
        return response.Response(msg, status.HTTP_200_OK)

    @decorators.action(methods=['post'], detail=True, url_path='operation')
    def operation(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        cryptocurrencie = self.get_object()
        amount_of_cryptocurrencies = serializer.validated_data.get('amount')
        operation_type = serializer.validated_data.get('type')

        if operation_type == CryptocurrencyOperationTypeChoices.BUY:
            params_cryptocurrency_operation = {
                'buyer': get_object_or_404(User, pk=kwargs.get('user_pk')),
                'seller': get_object_or_404(User, pk=serializer.validated_data.get('user_id'))
            }
        else:
            # SELL
            params_cryptocurrency_operation = {
                'buyer': get_object_or_404(User, pk=serializer.validated_data.get('user_id')),
                'seller': get_object_or_404(User, pk=kwargs.get('user_pk'))
            }

        successful_purchase, msg = CryptocurrencyOperationService.execute(
            **{
                **params_cryptocurrency_operation,
                'cryptocurrencie': cryptocurrencie,
                'amount_of_cryptocurrencies': amount_of_cryptocurrencies,
                'operation_type': operation_type
            }
        )

        if not successful_purchase:
            raise ValidationError(msg)

        return response.Response({msg}, status.HTTP_201_CREATED)
