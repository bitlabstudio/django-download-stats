"""Views for the ``download_stats`` app."""
import os

from django.conf import settings
from django.db.models import F
from django.http import Http404, HttpResponse
from django.views.generic import View
from django.utils.encoding import smart_str

from .models import DownloadStatistic


class DownloadView(View):
    """View that increments download counts and serves the files."""
    def dispatch(self, request, *args, **kwargs):
        self.requested_file = kwargs.get('requested_file')
        self.file_name = os.path.basename(self.requested_file)
        self.full_file_path = os.path.join(settings.MEDIA_ROOT,
                                           self.requested_file)
        if not self.requested_file or not os.path.exists(self.full_file_path):
            raise Http404

        return super(DownloadView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        with open(self.full_file_path) as f:
            response = HttpResponse(content=f.read(),
                                    content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename={}'.format(
            smart_str(self.file_name))
        # the usual case is that there is already at least one download of a
        # file, so only on creation we would trigger an additional query
        if not DownloadStatistic.objects.filter(
                download_url=self.full_file_path).update(count=F('count')+1):
            DownloadStatistic.objects.create(download_url=self.full_file_path,
                                             count=1)
        return response
