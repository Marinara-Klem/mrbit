from django.urls import path, include

from .routes import router_urls

app_name = 'api'

urlpatterns = [
    path('docs/', include("project.urls.api.docs")),
]

urlpatterns += router_urls
