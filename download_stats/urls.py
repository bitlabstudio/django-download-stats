"""URLs for the ``download_stats`` app."""
from django.conf.urls.defaults import patterns, url

from .settings import DOWNLOAD_URL
from .views import DownloadView


urlpatterns = patterns(
    '',
    url(r'{}/(?P<requested_file>.+)'.format(DOWNLOAD_URL.replace('/', '')),
        DownloadView.as_view(),
        name='download_view'),
)
