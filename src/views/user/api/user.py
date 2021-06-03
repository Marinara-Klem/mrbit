from rest_framework import viewsets

from domain.user.models import User
from views.user.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
