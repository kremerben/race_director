# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RaceSeries'
        db.create_table(u'results_raceseries', (
            (u'basemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['results.BaseModel'], unique=True, primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('contact_phone', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('info_document', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=120, null=True, blank=True)),
            ('host_club', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='host_club', null=True, to=orm['results.Club'])),
        ))
        db.send_create_signal(u'results', ['RaceSeries'])

        # Adding model 'Racer'
        db.create_table(u'results_racer', (
            (u'basemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['results.BaseModel'], unique=True, primary_key=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('birthdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('club', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='racer_club', null=True, to=orm['results.Club'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'results', ['Racer'])

        # Adding model 'Race'
        db.create_table(u'results_race', (
            (u'basemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['results.BaseModel'], unique=True, primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 7, 10, 0, 0))),
            ('start_time', self.gf('django.db.models.fields.TimeField')(default='10:00')),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('fee', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('contact_phone', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('info_document', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('result_document', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=120, null=True, blank=True)),
            ('race_series', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='race_series', null=True, to=orm['results.RaceSeries'])),
        ))
        db.send_create_signal(u'results', ['Race'])

        # Adding model 'Result'
        db.create_table(u'results_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('racer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='racer', to=orm['results.Racer'])),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(related_name='race', to=orm['results.Race'])),
            ('start_time', self.gf('django.db.models.fields.TimeField')(default='9:00')),
            ('finish_time', self.gf('django.db.models.fields.TimeField')()),
            ('place', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'results', ['Result'])

        # Adding model 'Club'
        db.create_table(u'results_club', (
            (u'basemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['results.BaseModel'], unique=True, primary_key=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=120, null=True, blank=True)),
        ))
        db.send_create_signal(u'results', ['Club'])

        # Adding model 'BaseModel'
        db.create_table(u'results_basemodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'results', ['BaseModel'])


    def backwards(self, orm):
        # Deleting model 'RaceSeries'
        db.delete_table(u'results_raceseries')

        # Deleting model 'Racer'
        db.delete_table(u'results_racer')

        # Deleting model 'Race'
        db.delete_table(u'results_race')

        # Deleting model 'Result'
        db.delete_table(u'results_result')

        # Deleting model 'Club'
        db.delete_table(u'results_club')

        # Deleting model 'BaseModel'
        db.delete_table(u'results_basemodel')


    models = {
        u'results.basemodel': {
            'Meta': {'object_name': 'BaseModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'results.club': {
            'Meta': {'object_name': 'Club', '_ormbases': [u'results.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['results.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'})
        },
        u'results.race': {
            'Meta': {'object_name': 'Race', '_ormbases': [u'results.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['results.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 7, 10, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'fee': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'info_document': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'race_series': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'race_series'", 'null': 'True', 'to': u"orm['results.RaceSeries']"}),
            'result_document': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'default': "'10:00'"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'})
        },
        u'results.racer': {
            'Meta': {'object_name': 'Racer', '_ormbases': [u'results.BaseModel']},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['results.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'club': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'racer_club'", 'null': 'True', 'to': u"orm['results.Club']"}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'})
        },
        u'results.raceseries': {
            'Meta': {'object_name': 'RaceSeries', '_ormbases': [u'results.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['results.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'host_club': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'host_club'", 'null': 'True', 'to': u"orm['results.Club']"}),
            'info_document': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'})
        },
        u'results.result': {
            'Meta': {'object_name': 'Result'},
            'finish_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.IntegerField', [], {}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'race'", 'to': u"orm['results.Race']"}),
            'racer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'racer'", 'to': u"orm['results.Racer']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {'default': "'9:00'"})
        }
    }

    complete_apps = ['results']