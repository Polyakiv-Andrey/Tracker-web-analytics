from django.db import models

from apis.campaigns.models import Campaigns


class Offers(models.Model):
    title = models.CharField(max_length=300)
    url = models.URLField()
    campaigns = models.ForeignKey(Campaigns, on_delete=models.CASCADE, related_name="offers")

    def __str__(self):
        return self.title
