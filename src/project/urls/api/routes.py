from rest_framework.routers import SimpleRouter

from views.cryptocurrencie.api import CryptocurrencieViewSet
from views.user.api import UserViewSet

router = SimpleRouter()

router.register('users', UserViewSet)
router.register('cryptocurrencies', CryptocurrencieViewSet)

router_urls = router.urls
