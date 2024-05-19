from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from apis.offers.filters import OffersFilter
from apis.offers.models import Offers
from apis.offers.serializers import OffersSerializer


class OffersAPIViewSet(viewsets.ModelViewSet):
    serializer_class = OffersSerializer
    queryset = Offers.objects.all()
    permission_classes = [permissions.AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OffersFilter
