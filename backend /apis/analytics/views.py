from datetime import timedelta

from django.db.models import Count, Sum
from django.db.models.functions import TruncDay
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from apis.click.models import Click
from apis.leads.models import Lead


class ClickStatisticsView(APIView):
    queryset = Click.objects.all()

    def get(self, request, *args, **kwargs):
        today = timezone.now().date()
        one_week_ago = today - timedelta(days=6)

        date_list = [(one_week_ago + timedelta(days=i)) for i in range(7)]

        clicks_last_week = (
            Click.objects.filter(click_time__date__gte=one_week_ago)
            .annotate(day=TruncDay('click_time'))
            .values('day')
            .annotate(count=Count('id'))
            .order_by('day')
        )

        click_dict = {click['day'].date(): click['count'] for click in clicks_last_week}

        clicks_last_week_filled = [
            {
                'day': day,
                'table_name': 'Click amount',
                'statistic': click_dict.get(day, 0)
            }
            for day in date_list
        ]

        data = {
            'clicks_last_week': clicks_last_week_filled,
        }

        return Response(data)


class LeadStatisticsView(APIView):
    queryset = Lead.objects.all()

    def get(self, request, *args, **kwargs):
        today = timezone.now().date()
        one_week_ago = today - timedelta(days=6)

        date_list = [(one_week_ago + timedelta(days=i)) for i in range(7)]

        leads_last_week = (
            Lead.objects.filter(date__date__gte=one_week_ago)
            .annotate(day=TruncDay('date'))
            .values('day')
            .annotate(count=Count('id'))
            .order_by('day')
        )

        lead_dict = {lead['day'].date(): lead['count'] for lead in leads_last_week}

        leads_last_week_filled = [
            {
                'day': day,
                'table_name': 'Lead amount',
                'statistic': lead_dict.get(day, 0)
            }
            for day in date_list
        ]

        data = {
            'leads_last_week': leads_last_week_filled,
        }

        return Response(data)


class ConversionStatisticsView(APIView):
    queryset = Lead.objects.all()

    def get(self, request, *args, **kwargs):
        today = timezone.now().date()
        one_week_ago = today - timedelta(days=6)

        date_list = [(one_week_ago + timedelta(days=i)).isoformat() for i in range(7)]

        clicks_last_week = (
            Click.objects.filter(click_time__date__gte=one_week_ago)
            .annotate(day=TruncDay('click_time'))
            .values('day')
            .annotate(click_count=Count('id'))
            .order_by('day')
        )

        leads_last_week = (
            Lead.objects.filter(date__date__gte=one_week_ago)
            .annotate(day=TruncDay('date'))
            .values('day')
            .annotate(lead_count=Count('id'))
            .order_by('day')
        )

        click_dict = {click['day'].date().isoformat(): click['click_count'] for click in clicks_last_week}
        lead_dict = {lead['day'].date().isoformat(): lead['lead_count'] for lead in leads_last_week}

        conversions_last_week_filled = []
        for day in date_list:
            clicks = click_dict.get(day, 0)
            leads = lead_dict.get(day, 0)
            conversion_rate = (leads / clicks * 100) if clicks > 0 else 0
            conversions_last_week_filled.append(
                {
                    'day': day,
                    'table_name': 'Conversation rate',
                    'statistic': conversion_rate
                }
            )

        data = {
            'conversions_last_week': conversions_last_week_filled,
        }

        return Response(data)


class RevenueStatisticsView(APIView):
    queryset = Lead.objects.all()

    def get(self, request, *args, **kwargs):
        today = timezone.now().date()
        one_week_ago = today - timedelta(days=6)

        date_list = [(one_week_ago + timedelta(days=i)).isoformat() for i in range(7)]

        leads_last_week = (
            Lead.objects.filter(date__date__gte=one_week_ago)
            .annotate(day=TruncDay('date'))
            .values('day')
            .annotate(total_revenue=Sum('revenue'))
            .order_by('day')
        )

        revenue_dict = {lead['day'].date().isoformat(): lead['total_revenue'] for lead in leads_last_week}

        revenue_last_week_filled = [
            {
                'day': day,
                'table_name': 'Total revenue',
                'statistic': revenue_dict.get(day, 0.0)
            }
            for day in date_list
        ]

        data = {
            'revenue_last_week': revenue_last_week_filled,
        }

        return Response(data)


class EPCStatisticsView(APIView):
    queryset = Click.objects.all()

    def get(self, request, *args, **kwargs):
        today = timezone.now().date()
        one_week_ago = today - timedelta(days=6)

        date_list = [(one_week_ago + timedelta(days=i)).isoformat() for i in range(7)]

        clicks_last_week = (
            Click.objects.filter(click_time__date__gte=one_week_ago)
            .annotate(day=TruncDay('click_time'))
            .values('day')
            .annotate(click_count=Count('id'))
            .order_by('day')
        )

        leads_last_week = (
            Lead.objects.filter(date__date__gte=one_week_ago)
            .annotate(day=TruncDay('date'))
            .values('day')
            .annotate(total_revenue=Sum('revenue'))
            .order_by('day')
        )

        click_dict = {click['day'].date().isoformat(): click['click_count'] for click in clicks_last_week}
        revenue_dict = {lead['day'].date().isoformat(): lead['total_revenue'] for lead in leads_last_week}

        cumulative_clicks = 0
        cumulative_revenue = 0.0
        epc_last_week_filled = []

        for day in date_list:
            clicks = click_dict.get(day, 0)
            revenue = revenue_dict.get(day, 0.0)

            cumulative_clicks += clicks
            cumulative_revenue += revenue

            epc = (cumulative_revenue / cumulative_clicks) if cumulative_clicks > 0 else 0.0

            epc_last_week_filled.append({
                'day': day,
                'table_name': 'EPC',
                'statistic': epc
            })

        data = {
            'epc_last_week': epc_last_week_filled,
        }

        return Response(data)