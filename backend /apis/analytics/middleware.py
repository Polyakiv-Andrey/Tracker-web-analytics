import re

from apis.click.models import Click


class AnalyticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        ip_address = self.get_client_ip(request)
        operating_system = self.get_operating_system(user_agent)

        click = Click(
            click_url=request.build_absolute_uri(),
            user_agent=user_agent,
            ip_address=ip_address,
            operating_system=operating_system
        )
        click.save()

        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get_operating_system(self, user_agent):
        os_patterns = [
            ('Windows', 'Windows'),
            ('Mac OS', 'Mac OS'),
            ('Linux', 'Linux'),
            ('Android', 'Android'),
            ('iOS', 'iOS'),
        ]
        for pattern, name in os_patterns:
            if re.search(pattern, user_agent, re.IGNORECASE):
                return name
        return 'Unknown'
