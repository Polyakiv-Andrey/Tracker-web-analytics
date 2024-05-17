from django.urls import path, include
from rest_framework.routers import SimpleRouter

from apis.offers.views import (
    OffersAPIViewSet
)

router = SimpleRouter()
router.register(r'offers', OffersAPIViewSet, basename='offers')

urlpatterns = [
    path('', include(router.urls)),
]


app_name = "offers"
