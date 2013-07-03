"""Admin classes for the ``download_stats`` app."""
from django.contrib import admin

from .models import DownloadStatistic


class DownloadStatisticAdmin(admin.ModelAdmin):
    """Custom admin for the ``DownloadStatistic`` model."""
    list_display = ('download_url', 'count')
    search_fields = ['download_url', ]


admin.site.register(DownloadStatistic, DownloadStatisticAdmin)
