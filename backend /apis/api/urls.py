from django.urls import path, include


urlpatterns = [
    path("", include("apis.campaigns.urls", namespace="campaigns")),
    path("", include("apis.offers.urls", namespace="offers")),
    path("", include("apis.click.urls", namespace="clicks")),
    path("", include("apis.leads.urls", namespace="leads")),
]
