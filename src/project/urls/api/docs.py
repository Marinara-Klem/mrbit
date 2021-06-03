from django.urls import path
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Mrbit",
        default_version='v1'
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

app_name = 'docs'
urlpatterns = [
    path('', RedirectView.as_view(pattern_name='api:docs:schema-swagger-ui'), name='docs-v1'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
