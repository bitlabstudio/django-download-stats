# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DownloadStatistic'
        db.create_table(u'download_stats_downloadstatistic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('download_url', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('count', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'download_stats', ['DownloadStatistic'])


    def backwards(self, orm):
        # Deleting model 'DownloadStatistic'
        db.delete_table(u'download_stats_downloadstatistic')


    models = {
        u'download_stats.downloadstatistic': {
            'Meta': {'object_name': 'DownloadStatistic'},
            'count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'download_url': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['download_stats']
