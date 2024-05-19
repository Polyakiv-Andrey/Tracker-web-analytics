from django.db import models


class Lead(models.Model):
    INTEREST_LEVEL_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]

    user = models.CharField(max_length=300)
    action = models.CharField(max_length=1024)
    date = models.DateTimeField()
    interest_level = models.CharField(max_length=10, choices=INTEREST_LEVEL_CHOICES, default='medium')
    revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.user


