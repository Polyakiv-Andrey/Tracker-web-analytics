from rest_framework import serializers

from apis.campaigns.serializers import CampaignsSerializer
from apis.offers.models import Offers


class OffersSerializer(serializers.ModelSerializer):
    campaigns = CampaignsSerializer()

    class Meta:
        model = Offers
        fields = ["id", "title", "url", "campaigns"]