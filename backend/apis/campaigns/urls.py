from django.urls import path, include
from rest_framework.routers import SimpleRouter

from apis.campaigns.views import (
    CampaignsAPIViewSet
)

router = SimpleRouter()
router.register(r'campaigns', CampaignsAPIViewSet, basename='campaigns')

urlpatterns = [
    path('', include(router.urls)),
]


app_name = "campaigns"
