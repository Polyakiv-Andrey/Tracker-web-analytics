from rest_framework import serializers

from apis.campaigns.models import Campaigns
from apis.campaigns.serializers import CampaignsSerializer
from apis.offers.models import Offers


class OffersSerializer(serializers.ModelSerializer):
    campaigns = serializers.PrimaryKeyRelatedField(queryset=Campaigns.objects.all(), write_only=True)
    campaigns_detail = serializers.SerializerMethodField()

    class Meta:
        model = Offers
        fields = ["id", "title", "url", "campaigns", "campaigns_detail"]
        read_only_fields = ["campaigns_detail", "id"]

    def get_campaigns_detail(self, obj):
        return CampaignsSerializer(obj.campaigns).data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['campaigns'] = representation.pop('campaigns_detail')
        return representation
    