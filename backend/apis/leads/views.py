from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from apis.leads.filters import LeadsFilter
from apis.leads.models import Lead
from apis.leads.serializers import LeadSerializer


class LeadAPIViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    permission_classes = [permissions.AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = LeadsFilter
