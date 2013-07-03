"""Models of the ``download_stats`` app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _


class DownloadStatistic(models.Model):
    """
    Holds the information about how often a certain file was downloaded.

    :download_url: The URL from where the file was downloaded.
    :count: The amount of times this URL was clicked.

    """

    download_url = models.CharField(
        verbose_name=_('Download URL'),
        max_length=512,
    )

    count = models.PositiveIntegerField(
        verbose_name=_('Count'),
    )

    def __unicode__(self):
        return '{} ({})'.format(
            self.download_url[:50] + '...' if len(self.download_url) > 50
            else self.download_url, self.count)
