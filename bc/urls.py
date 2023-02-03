from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("bc.web.urls")),
    path("", include("bc.core.urls")),
    path("", include("bc.channel.urls")),
    path("", include("bc.subscription.urls")),
    path("django-rq/", include("django_rq.urls")),
]