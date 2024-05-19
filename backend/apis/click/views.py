from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions

from apis.click.filters import ClickFilter
from apis.click.models import Click
from apis.click.serializers import ClickSerializer


class ClickCreateListAPIView(generics.ListCreateAPIView):
    serializer_class = ClickSerializer
    queryset = Click.objects.all()
    permission_classes = [permissions.AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ClickFilter


class ClickRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ClickSerializer
    queryset = Click.objects.all()
    permission_classes = [permissions.AllowAny]
    lookup_field = "id"



