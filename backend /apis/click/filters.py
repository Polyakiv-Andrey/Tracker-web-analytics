import django_filters
from .models import Click


class ClickFilter(django_filters.FilterSet):
    click_time = django_filters.DateTimeFilter()
    click_time_range = django_filters.DateTimeFromToRangeFilter(field_name='click_time')
    click_url = django_filters.CharFilter(lookup_expr='icontains')
    user_agent = django_filters.CharFilter(lookup_expr='icontains')
    ip_address = django_filters.CharFilter(lookup_expr='exact')
    operating_system = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Click
        fields = ['click_time', 'click_url', 'user_agent', 'ip_address', 'operating_system']