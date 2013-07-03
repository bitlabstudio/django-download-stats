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
        self.requested_file = request.GET.get('file')
        self.file_name = os.path.basename(self.requested_file)
        # we construct the real path from the requested file
        self.full_file_path = os.path.realpath(
            os.path.join(settings.MEDIA_ROOT, self.requested_file))
        # then we check if it is a sub-path of MEDIA_ROOT
        # if not, we know, that someone tried to get some files from below the
        # media level. The files above the media root should be accessible
        # by default anyway
        self.full_file_url = os.path.join(settings.MEDIA_URL,
                                          self.requested_file)
        if (
                not self.full_file_path.startswith(os.path.realpath(
                    settings.MEDIA_ROOT))
                or not self.requested_file
                or not os.path.exists(self.full_file_path)
                or '..' in self.requested_file):
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
                download_url=self.full_file_url).update(count=F('count')+1):
            DownloadStatistic.objects.create(download_url=self.full_file_url,
                                             count=1)
        return response
