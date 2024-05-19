import django_filters

from apis.leads.models import Lead


class LeadsFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(lookup_expr='icontains')
    action = django_filters.CharFilter(lookup_expr='icontains')
    date = django_filters.DateTimeFilter(field_name='date', lookup_expr='gte')
    interest_level = django_filters.CharFilter(lookup_expr='icontains')
    ordering = django_filters.OrderingFilter(
        fields=(
            ('user', 'user'),
            ('action', 'action'),
            ('date', 'date'),
            ('interest_level', 'interest_level'),
        )
    )

    class Meta:
        model = Lead
        fields = ['user', 'action', 'date', 'interest_level', "ordering"]