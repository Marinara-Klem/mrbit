from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from views.cryptocurrencie.api import CryptocurrencieViewSet, CryptocurrencyOperationViewSet
from views.user.api import UserViewSet

router = SimpleRouter()

_users = 'users'
_cryptocurrencies = 'cryptocurrencies'

router.register(_users, UserViewSet)
router.register(_cryptocurrencies, CryptocurrencieViewSet)

user_router = routers.NestedSimpleRouter(router, _users, lookup='user')
user_router.register(_cryptocurrencies, CryptocurrencyOperationViewSet)

router_urls = router.urls + user_router.urls
