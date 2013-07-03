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

Define ``DOWNLOAD_URL`` in your settings if you want to override the default
of ``/downloads/``::

    DOWNLOAD_URL = "/my-download/"


Add the ``download_stats`` URLs to your ``urls.py``::

    urlpatterns = patterns('',
        ...
        url(r'^myurlname/', include('download_stats.urls')),
    )

An important note is, that the ``download_stats.urls`` will automatically
prepend the ``DOWNLOAD_URL`` setting. So the following urls example would
result in urls formatted like ``example.com/downloads/filename.jpg``
considering if you would leave the ``DOWNLOAD_URL`` on its default value
``/downloads/``.

    urlpatterns = patterns('',
        ...
        url(r'^', include('download_stats.urls')),
    )

Why this setting anyway then?
Because now you will add the context processor::

    TEMPLATE_CONTEXT_PROCESSORS = [
        ...
        'download_stats.context_processors.download_url',
    ]

This will add the ``DOWNLOAD_URL`` variable to all templates.

Don't forget to migrate your database::

    ./manage.py migrate download_stats


Usage
-----

With our context processor adding ``DOWNLOAD_URL`` you can basically use the
view that comes with download stats just like you would do it before, just
replacing ``MEDIA_URL`` with ``DOWNLOAD_URL``::

    <a href="{{ DOWNLOAD_URL }}files/myfile.pdf">Click to download my file</a>

It will then automatically count how often ``files/myfile.pdf`` was clicked.

You can then view the individual file counts in the download stats admin.


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
