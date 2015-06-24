# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'np_server_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('you_session', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('api_key', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal(u'np_server', ['UserProfile'])

        # Adding model 'PasswordType'
        db.create_table(u'np_server_passwordtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('for_date', self.gf('django.db.models.fields.DateField')()),
            ('url_site', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'np_server', ['PasswordType'])

        # Adding model 'ClientStatus'
        db.create_table(u'np_server_clientstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('alarm', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('warning', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blocking', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('privacy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('search_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('monitor_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'np_server', ['ClientStatus'])

        # Adding model 'Device'
        db.create_table(u'np_server_device', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('imei', self.gf('django.db.models.fields.CharField')(max_length=18)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('mac', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('usbidcode', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('height', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cell_id', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ip_info', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('wifi_info', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('battery_info', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('webcam_picture', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'np_server', ['Device'])

        # Adding model 'CellId'
        db.create_table(u'np_server_cellid', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('mcc', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
            ('mnc', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
            ('lac', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cid', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'np_server', ['CellId'])

        # Adding model 'Research'
        db.create_table(u'np_server_research', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('geo_info', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('wifi_info', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('webcam', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'np_server', ['Research'])

        # Adding model 'Action'
        db.create_table(u'np_server_action', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('alarm', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('warning', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blocking', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('privacy', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'np_server', ['Action'])

        # Adding model 'Report'
        db.create_table(u'np_server_report', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('all', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('report_text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'np_server', ['Report'])

        # Adding model 'OS'
        db.create_table(u'np_server_os', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_os', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('core', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'np_server', ['OS'])

        # Adding model 'SmsCommands'
        db.create_table(u'np_server_smscommands', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('alarm', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('message', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sound_on', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sound_off', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('speak', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_start', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_stop', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('wifi_start', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('wifi_stop', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('call', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hangup', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('recordsound', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('apn_copy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('apn_remove', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('apn_enable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('apn_disable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('gps_on', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('block', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unblock', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('startapp', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('erasesdcard', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('wipe', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'np_server', ['SmsCommands'])

        # Adding model 'UpdateDevice'
        db.create_table(u'np_server_updatedevice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('imei', self.gf('django.db.models.fields.CharField')(max_length=18)),
            ('date1', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 6, 24, 0, 0), blank=True)),
            ('latitude1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('longitude1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('height1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date2', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 6, 24, 0, 0), blank=True)),
            ('latitude2', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('longitude2', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('height2', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date3', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 6, 24, 0, 0), blank=True)),
            ('latitude3', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('longitude3', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('height3', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'np_server', ['UpdateDevice'])

        # Adding model 'Karma'
        db.create_table(u'np_server_karma', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('karma_index', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'np_server', ['Karma'])

        # Adding model 'Category'
        db.create_table(u'np_server_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category_name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('sub_category', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'np_server', ['Category'])

        # Adding model 'Status'
        db.create_table(u'np_server_status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('busyness', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sold', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('in_work', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('checking', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('draft', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('recoil', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('arbitration', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('finished', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'np_server', ['Status'])

        # Adding model 'Billing'
        db.create_table(u'np_server_billing', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('cost', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
            ('system_cost', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
            ('payment', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('history', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal(u'np_server', ['Billing'])

        # Adding model 'Task'
        db.create_table(u'np_server_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['np_server.Status'], null=True)),
            ('theme', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('task', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('term', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('cost', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
            ('karma', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['np_server.Karma'], null=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['np_server.Category'], null=True)),
        ))
        db.send_create_signal(u'np_server', ['Task'])

        # Adding model 'Customer'
        db.create_table(u'np_server_customer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['np_server.Task'], null=True)),
            ('billing', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['np_server.Billing'], null=True)),
        ))
        db.send_create_signal(u'np_server', ['Customer'])

        # Adding model 'Perfomer'
        db.create_table(u'np_server_perfomer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['np_server.Task'], null=True)),
            ('billing', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['np_server.Billing'], null=True)),
        ))
        db.send_create_signal(u'np_server', ['Perfomer'])

        # Adding model 'Order'
        db.create_table(u'np_server_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['np_server.Task'], null=True)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['np_server.Status'], null=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['np_server.Customer'], null=True)),
            ('perfomer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['np_server.Perfomer'], null=True)),
            ('cost', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
        ))
        db.send_create_signal(u'np_server', ['Order'])

        # Adding model 'Message'
        db.create_table(u'np_server_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['np_server.Customer'], null=True)),
            ('perfomer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['np_server.Perfomer'], null=True)),
            ('mes_room', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('mes_body', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal(u'np_server', ['Message'])

        # Adding model 'TaskCard'
        db.create_table(u'np_server_taskcard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['np_server.Task'], null=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['np_server.Customer'], null=True)),
            ('perfomer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['np_server.Perfomer'], null=True)),
            ('cost', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
        ))
        db.send_create_signal(u'np_server', ['TaskCard'])

        # Adding model 'DeviceList'
        db.create_table(u'np_server_devicelist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('device', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['np_server.Device'], null=True)),
            ('files_list', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('files_downloaded', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal(u'np_server', ['DeviceList'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'np_server_userprofile')

        # Deleting model 'PasswordType'
        db.delete_table(u'np_server_passwordtype')

        # Deleting model 'ClientStatus'
        db.delete_table(u'np_server_clientstatus')

        # Deleting model 'Device'
        db.delete_table(u'np_server_device')

        # Deleting model 'CellId'
        db.delete_table(u'np_server_cellid')

        # Deleting model 'Research'
        db.delete_table(u'np_server_research')

        # Deleting model 'Action'
        db.delete_table(u'np_server_action')

        # Deleting model 'Report'
        db.delete_table(u'np_server_report')

        # Deleting model 'OS'
        db.delete_table(u'np_server_os')

        # Deleting model 'SmsCommands'
        db.delete_table(u'np_server_smscommands')

        # Deleting model 'UpdateDevice'
        db.delete_table(u'np_server_updatedevice')

        # Deleting model 'Karma'
        db.delete_table(u'np_server_karma')

        # Deleting model 'Category'
        db.delete_table(u'np_server_category')

        # Deleting model 'Status'
        db.delete_table(u'np_server_status')

        # Deleting model 'Billing'
        db.delete_table(u'np_server_billing')

        # Deleting model 'Task'
        db.delete_table(u'np_server_task')

        # Deleting model 'Customer'
        db.delete_table(u'np_server_customer')

        # Deleting model 'Perfomer'
        db.delete_table(u'np_server_perfomer')

        # Deleting model 'Order'
        db.delete_table(u'np_server_order')

        # Deleting model 'Message'
        db.delete_table(u'np_server_message')

        # Deleting model 'TaskCard'
        db.delete_table(u'np_server_taskcard')

        # Deleting model 'DeviceList'
        db.delete_table(u'np_server_devicelist')


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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
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
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'np_server.action': {
            'Meta': {'object_name': 'Action'},
            'alarm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'blocking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'privacy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'warning': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'np_server.billing': {
            'Meta': {'object_name': 'Billing'},
            'cost': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'history': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'system_cost': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        },
        u'np_server.category': {
            'Meta': {'object_name': 'Category'},
            'category_name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sub_category': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'np_server.cellid': {
            'Meta': {'object_name': 'CellId'},
            'cid': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lac': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mcc': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'mnc': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        },
        u'np_server.clientstatus': {
            'Meta': {'object_name': 'ClientStatus'},
            'alarm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'blocking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'monitor_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'privacy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'warning': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'np_server.customer': {
            'Meta': {'object_name': 'Customer'},
            'billing': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['np_server.Billing']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['np_server.Task']", 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        },
        u'np_server.device': {
            'Meta': {'object_name': 'Device'},
            'battery_info': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'cell_id': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imei': ('django.db.models.fields.CharField', [], {'max_length': '18'}),
            'ip_info': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'usbidcode': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'webcam_picture': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'wifi_info': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'np_server.devicelist': {
            'Meta': {'object_name': 'DeviceList'},
            'device': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['np_server.Device']", 'null': 'True'}),
            'files_downloaded': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'files_list': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        },
        u'np_server.karma': {
            'Meta': {'object_name': 'Karma'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'karma_index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        },
        u'np_server.message': {
            'Meta': {'object_name': 'Message'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['np_server.Customer']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mes_body': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'mes_room': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'perfomer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['np_server.Perfomer']", 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        },
        u'np_server.order': {
            'Meta': {'object_name': 'Order'},
            'cost': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['np_server.Customer']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perfomer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['np_server.Perfomer']", 'null': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['np_server.Status']", 'null': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['np_server.Task']", 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        },
        u'np_server.os': {
            'Meta': {'object_name': 'OS'},
            'core': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_os': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'np_server.passwordtype': {
            'Meta': {'object_name': 'PasswordType'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'for_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url_site': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'np_server.perfomer': {
            'Meta': {'object_name': 'Perfomer'},
            'billing': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['np_server.Billing']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['np_server.Task']", 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        },
        u'np_server.report': {
            'Meta': {'object_name': 'Report'},
            'all': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report_text': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        },
        u'np_server.research': {
            'Meta': {'object_name': 'Research'},
            'geo_info': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'webcam': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wifi_info': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'np_server.smscommands': {
            'Meta': {'object_name': 'SmsCommands'},
            'alarm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'apn_copy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'apn_disable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'apn_enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'apn_remove': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'block': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'call': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'data_start': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'data_stop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'erasesdcard': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gps_on': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hangup': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'recordsound': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sound_off': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sound_on': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'speak': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'startapp': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unblock': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'wifi_start': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wifi_stop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wipe': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'np_server.status': {
            'Meta': {'object_name': 'Status'},
            'arbitration': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'busyness': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'checking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'draft': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'finished': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_work': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'recoil': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sold': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        },
        u'np_server.task': {
            'Meta': {'object_name': 'Task'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['np_server.Category']", 'null': 'True'}),
            'cost': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'karma': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['np_server.Karma']", 'null': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['np_server.Status']", 'null': 'True'}),
            'task': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'term': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'theme': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        },
        u'np_server.taskcard': {
            'Meta': {'object_name': 'TaskCard'},
            'cost': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['np_server.Customer']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perfomer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['np_server.Perfomer']", 'null': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['np_server.Task']", 'null': 'True'})
        },
        u'np_server.updatedevice': {
            'Meta': {'object_name': 'UpdateDevice'},
            'date1': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 6, 24, 0, 0)', 'blank': 'True'}),
            'date2': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 6, 24, 0, 0)', 'blank': 'True'}),
            'date3': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 6, 24, 0, 0)', 'blank': 'True'}),
            'height1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'height2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'height3': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imei': ('django.db.models.fields.CharField', [], {'max_length': '18'}),
            'latitude1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'latitude2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'latitude3': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'longitude1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'longitude2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'longitude3': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'np_server.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'api_key': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'you_session': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        }
    }

    complete_apps = ['np_server']