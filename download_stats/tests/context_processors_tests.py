"""Tests for the context processors of the ``download_stats`` app."""
from django.test import TestCase

from ..context_processors import download_url


class DownloadURLTestCase(TestCase):
    """Tests for the ``download_url`` context processor."""
    longMessage = True

    def test_download_url(self):
        self.assertEqual(download_url({}), {'DOWNLOAD_URL': '/downloads/'})
