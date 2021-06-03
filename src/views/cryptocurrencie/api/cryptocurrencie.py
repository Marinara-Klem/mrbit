from rest_framework import viewsets, decorators

from domain.cryptocurrencie.models import Cryptocurrencie, Wallet
from views.cryptocurrencie.serializer import CryptocurrencieSerializer, WalletSerializer


class CryptocurrencieViewSet(viewsets.ModelViewSet):
    serializer_class = CryptocurrencieSerializer
    queryset = Cryptocurrencie.objects.all()


class CryptocurrencieBuySaleViewSet(viewsets.ModelViewSet):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()
