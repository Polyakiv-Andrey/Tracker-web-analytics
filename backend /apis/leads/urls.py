from django.urls import path, include
from rest_framework.routers import SimpleRouter

from apis.leads.views import (
    LeadAPIViewSet
)

router = SimpleRouter()
router.register(r'leads', LeadAPIViewSet, basename='leads')

urlpatterns = [
    path('', include(router.urls)),
]


app_name = "leads"
