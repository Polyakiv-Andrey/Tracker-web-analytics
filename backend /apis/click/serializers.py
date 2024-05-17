from rest_framework import serializers

from apis.click.models import Click


class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = "__all__"
