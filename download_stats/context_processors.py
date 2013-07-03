"""Context processors of the ``download_stats`` app."""
from .settings import DOWNLOAD_URL


def download_url(request):
    """Adds the DOWNLOAD_URL setting to the context."""
    return {'DOWNLOAD_URL': DOWNLOAD_URL}
