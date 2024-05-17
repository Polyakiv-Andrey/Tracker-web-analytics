import django_filters
from .models import Campaigns


class CampaignFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    goal = django_filters.CharFilter(lookup_expr='icontains')
    start_date_after = django_filters.DateTimeFilter(field_name='start_date', lookup_expr='gte')
    start_date_before = django_filters.DateTimeFilter(field_name='start_date', lookup_expr='lte')
    end_date_after = django_filters.DateTimeFilter(field_name='end_date', lookup_expr='gte')
    end_date_before = django_filters.DateTimeFilter(field_name='end_date', lookup_expr='lte')

    class Meta:
        model = Campaigns
        fields = ['name', 'start_date', 'end_date', 'goal']