from rest_framework import viewsets

from domain.cryptocurrencie.models import Cryptocurrencie
from views.cryptocurrencie.serializer import CryptocurrencieSerializer


class CryptocurrencieViewSet(viewsets.ModelViewSet):
    serializer_class = CryptocurrencieSerializer
    queryset = Cryptocurrencie.objects.all()
