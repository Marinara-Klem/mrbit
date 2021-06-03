from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='api:docs:schema-swagger-ui')),

    # API base url
    path('api/v1/', include("project.urls.api.base", namespace='api')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
