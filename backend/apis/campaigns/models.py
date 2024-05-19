from django.db import models
from django.core.exceptions import ValidationError


class Campaigns(models.Model):
    name = models.CharField(max_length=300)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    goal = models.TextField()

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        if self.start_date >= self.end_date:
            raise ValidationError('The start date must be before the end date.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)