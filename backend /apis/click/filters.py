import django_filters
from .models import Click


class ClickFilter(django_filters.FilterSet):
    click_date_gte = django_filters.DateTimeFilter(field_name="click_time", lookup_expr="gte")
    click_date_lte = django_filters.DateTimeFilter(field_name="click_time", lookup_expr="lte")
    click_url = django_filters.CharFilter(lookup_expr='icontains')
    user_agent = django_filters.CharFilter(lookup_expr='icontains')
    ip_address = django_filters.CharFilter(lookup_expr='exact')
    operating_system = django_filters.CharFilter(lookup_expr='icontains')
    ordering = django_filters.OrderingFilter(
        fields=(
            ('click_time', 'click_time'),
            ('click_url', 'click_url'),
            ('user_agent', 'user_agent'),
            ('ip_address', 'ip_address'),
            ('operating_system', 'operating_system'),
        )
    )

    class Meta:
        model = Click
        fields = [
            'click_date_gte', 'click_date_lte', 'click_url', 'user_agent',
            'ip_address', 'operating_system', 'ordering'
        ]