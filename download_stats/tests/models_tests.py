"""Tests for the models of the ``download_stats`` app."""
from django.test import TestCase

from .factories import DownloadStatisticFactory


class DownloadStatisticTestCase(TestCase):
    """Tests for the ``DownloadStatistic`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instantiation of the ``DownloadStatistic`` model."""
        downloadstatistic = DownloadStatisticFactory()
        self.assertTrue(downloadstatistic.pk)
