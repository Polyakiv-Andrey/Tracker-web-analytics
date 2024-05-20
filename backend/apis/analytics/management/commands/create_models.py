import random
from datetime import datetime, timedelta, timezone

from django.core.management.base import BaseCommand
from apis.campaigns.models import Campaigns
from apis.click.models import Click
from apis.leads.models import Lead
from apis.offers.models import Offers


class Command(BaseCommand):
    help = 'Create models instances'

    def handle(self, *args, **kwargs):
        def random_date(start, end):
            return start + timedelta(
                seconds=random.randint(0, int((end - start).total_seconds())),
            )

        tz = timezone.utc

        today = datetime.now(tz)
        seven_days_ago = today - timedelta(days=7)

        for i in range(15):
            start_date = random_date(seven_days_ago, today)
            end_date = random_date(start_date, today)
            click_time = random_date(seven_days_ago, today)
            lead_date = random_date(seven_days_ago, today)

            campaigns = Campaigns.objects.create(
                name=f"Campaign {i + 1}",
                start_date=start_date,
                end_date=end_date,
                goal=f"Goal {i + 1}"
            )

            Click.objects.create(
                click_time=click_time,
                click_url=f"https://example.com/{i + 1}",
                user_agent=f"UserAgent {i + 1}",
                ip_address=f"192.168.1.{i + 1}",
                operating_system=f"OS {i + 1}"
            )

            Lead.objects.create(
                user=f"User {i + 1}",
                action="Buy",
                date=lead_date,
                interest_level=random.choice(["low", "medium", "high"]),
                revenue=random.randint(10, 1000)
            )

            Offers.objects.create(
                title=f"Offer {i + 1}",
                url=f"https://offer.com/{i + 1}",
                campaigns=campaigns
            )
        self.stdout.write(self.style.SUCCESS('Successfully created 15 instances for each model.'))

