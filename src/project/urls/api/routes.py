from rest_framework.routers import SimpleRouter

from views.user.api import UserViewSet

router = SimpleRouter()

router.register('users', UserViewSet)

router_urls = router.urls
