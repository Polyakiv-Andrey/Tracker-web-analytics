import django_filters
from .models import Campaigns


class CampaignFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    goal = django_filters.CharFilter(lookup_expr='icontains')
    start_date = django_filters.DateTimeFilter(field_name='start_date', lookup_expr='gte')
    end_date = django_filters.DateTimeFilter(field_name='end_date', lookup_expr='lte')
    ordering = django_filters.OrderingFilter(
        fields=(
            ('name', 'name'),
            ('goal', 'goal'),
            ('start_date', 'start_date'),
            ('end_date', 'end_date'),
        )
    )

    class Meta:
        model = Campaigns
        fields = ['name', 'start_date', 'end_date', 'goal', "ordering"]