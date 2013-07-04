"""Factories for the ``download_stats`` app."""
import factory

from ..models import DownloadStatistic


class DownloadStatisticFactory(factory.Factory):
    """Factory for the ``DownloadStatistic`` model."""
    FACTORY_FOR = DownloadStatistic

    download_url = factory.Sequence(lambda n: 'url-{}'.format(n))
