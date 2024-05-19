import django_filters

from apis.offers.models import Offers


class OffersFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    url = django_filters.CharFilter(lookup_expr='icontains')
    campaigns = django_filters.CharFilter(field_name='campaigns__name', lookup_expr='icontains')
    ordering = django_filters.OrderingFilter(
        fields=(
            ('title', 'title'),
            ('url', 'url'),
            ('campaigns', 'campaigns'),
        )
    )

    class Meta:
        model = Offers
        fields = ['title', 'url', 'campaigns', "ordering"]