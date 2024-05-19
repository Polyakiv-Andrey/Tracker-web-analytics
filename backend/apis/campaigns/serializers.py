from rest_framework import serializers

from apis.campaigns.models import Campaigns


class CampaignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaigns
        fields = ["id", "name", "start_date", "end_date", "goal"]