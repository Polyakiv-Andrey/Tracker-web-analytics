from rest_framework import viewsets, permissions

from apis.campaigns.models import Campaigns
from apis.campaigns.serializers import CampaignsSerializer


class CampaignsAPIViewSet(viewsets.ModelViewSet):
    serializer_class = CampaignsSerializer
    queryset = Campaigns.objects.all()
    permission_classes = [permissions.AllowAny]