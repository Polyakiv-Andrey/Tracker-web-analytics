from django.urls import path, include


urlpatterns = [
    path("campaigns/", include("apis.campaigns.urls", namespace="campaigns")),
]
