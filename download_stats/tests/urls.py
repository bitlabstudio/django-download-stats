"""URLs to run the tests."""
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url('^$', lambda r: HttpResponse('<a href="/downloads/?file=../test_requirements.txt">TEST</a>'), name='dummy_home'),  # NOQA
    url(r'^', include('download_stats.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (r'%s(?P<path>.*)' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),  # NOQA
    )
