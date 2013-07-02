Django Download Stats
=====================

A reusable Django app to keep track of file download statistics.

Installation
------------

To get the latest stable release from PyPi::

    $ pip install django-download-stats

To get the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/django-download-stats.git#egg=download_stats


Add ``download_stats`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'download_stats',
    )

Add the ``download_stats`` URLs to your ``urls.py``::

    urlpatterns = patterns('',
        ...
        url(r'^downloads/', include('download_stats.urls')),
    )

Don't forget to migrate your database::

    ./manage.py migrate download_stats


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps::

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 django-download-stats
    $ python setup.py install
    $ pip install -r dev_requirements.txt

    $ git co -b feature_branch master
    # Implement your feature and tests
    $ git add . && git commit
    $ git push -u origin feature_branch
    # Send us a pull request for your feature branch
