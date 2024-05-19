from django.urls import path

from apis.analytics.views import (
    ClickStatisticsView,
    LeadStatisticsView,
    ConversionStatisticsView,
    RevenueStatisticsView,
    EPCStatisticsView
)
urlpatterns = [
    path('clicks/', ClickStatisticsView.as_view(), name='click-statistic'),
    path('leads/', LeadStatisticsView.as_view(), name='lead-statistic'),
    path('conversions/', ConversionStatisticsView.as_view(), name='conversion-statistics'),
    path('revenue/', RevenueStatisticsView.as_view(), name='revenue-statistics'),
    path('epc/', EPCStatisticsView.as_view(), name='epc-statistics'),
]

app_name = "analytics"
