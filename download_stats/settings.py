"""Settings of the ``download_stats`` app."""
from django.conf import settings


DOWNLOAD_URL = getattr(settings, 'DOWNLOAD_URL', '/downloads/')
