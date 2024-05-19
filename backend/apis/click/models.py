from django.db import models


class Click(models.Model):
    click_time = models.DateTimeField(auto_now_add=True)
    click_url = models.URLField()
    user_agent = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    operating_system = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.click_url


