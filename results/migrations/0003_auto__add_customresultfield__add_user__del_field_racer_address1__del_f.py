# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CustomResultField'
        db.create_table(u'results_customresultfield', (
            (u'basemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['results.BaseModel'], unique=True, primary_key=True)),
            ('custom_field_value', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('custom_result', self.gf('django.db.models.fields.related.ForeignKey')(related_name='custom_result', to=orm['results.Result'])),
        ))
        db.send_create_signal(u'results', ['CustomResultField'])

        # Adding model 'User'
        db.create_table(u'results_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
        ))
        db.send_create_signal(u'results', ['User'])

        # Adding M2M table for field groups on 'User'
        m2m_table_name = db.shorten_name(u'results_user_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'results.user'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'User'
        m2m_table_name = db.shorten_name(u'results_user_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'results.user'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'permission_id'])

        # Deleting field 'Racer.address1'
        db.delete_column(u'results_racer', 'address1')

        # Deleting field 'Racer.address2'
        db.delete_column(u'results_racer', 'address2')

        # Deleting field 'Racer.phone'
        db.delete_column(u'results_racer', 'phone')

        # Deleting field 'Racer.city'
        db.delete_column(u'results_racer', 'city')

        # Deleting field 'Racer.zip'
        db.delete_column(u'results_racer', 'zip')

        # Deleting field 'Racer.note'
        db.delete_column(u'results_racer', 'note')

        # Deleting field 'Racer.state'
        db.delete_column(u'results_racer', 'state')

        # Deleting field 'Racer.country'
        db.delete_column(u'results_racer', 'country')

        # Deleting field 'Racer.email'
        db.delete_column(u'results_racer', 'email')

        # Adding field 'Racer.hometown'
        db.add_column(u'results_racer', 'hometown',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=120, blank=True),
                      keep_default=False)

        # Adding field 'Racer.user'
        db.add_column(u'results_racer', 'user',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['results.User'], unique=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'CustomResultField'
        db.delete_table(u'results_customresultfield')

        # Deleting model 'User'
        db.delete_table(u'results_user')

        # Removing M2M table for field groups on 'User'
        db.delete_table(db.shorten_name(u'results_user_groups'))

        # Removing M2M table for field user_permissions on 'User'
        db.delete_table(db.shorten_name(u'results_user_user_permissions'))

        # Adding field 'Racer.address1'
        db.add_column(u'results_racer', 'address1',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=120, blank=True),
                      keep_default=False)

        # Adding field 'Racer.address2'
        db.add_column(u'results_racer', 'address2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=120, blank=True),
                      keep_default=False)

        # Adding field 'Racer.phone'
        db.add_column(u'results_racer', 'phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=120, blank=True),
                      keep_default=False)

        # Adding field 'Racer.city'
        db.add_column(u'results_racer', 'city',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=120, blank=True),
                      keep_default=False)

        # Adding field 'Racer.zip'
        db.add_column(u'results_racer', 'zip',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=120, blank=True),
                      keep_default=False)

        # Adding field 'Racer.note'
        db.add_column(u'results_racer', 'note',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Racer.state'
        db.add_column(u'results_racer', 'state',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=120, blank=True),
                      keep_default=False)

        # Adding field 'Racer.country'
        db.add_column(u'results_racer', 'country',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=120, blank=True),
                      keep_default=False)

        # Adding field 'Racer.email'
        db.add_column(u'results_racer', 'email',
                      self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Racer.hometown'
        db.delete_column(u'results_racer', 'hometown')

        # Deleting field 'Racer.user'
        db.delete_column(u'results_racer', 'user_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        u'results.customresultfield': {
            'Meta': {'object_name': 'CustomResultField', '_ormbases': [u'results.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['results.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'custom_field_value': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'custom_result': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'custom_result'", 'to': u"orm['results.Result']"})
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
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['results.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'club': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'racer_club'", 'null': 'True', 'to': u"orm['results.Club']"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'hometown': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['results.User']", 'unique': 'True'})
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
        },
        u'results.user': {
            'Meta': {'object_name': 'User'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'})
        }
    }

    complete_apps = ['results']