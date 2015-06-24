# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ChatDialog.user2'
        db.delete_column(u'np_server_chatdialog', 'user2_id')

        # Deleting field 'ChatDialog.user1'
        db.delete_column(u'np_server_chatdialog', 'user1_id')

        # Adding field 'ChatDialog.user'
        db.add_column(u'np_server_chatdialog', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='+', to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'ChatDialog.interlocutor'
        db.add_column(u'np_server_chatdialog', 'interlocutor',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='+', to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'ChatMessage.dialog'
        db.delete_column(u'np_server_chatmessage', 'dialog_id')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'ChatDialog.user2'
        raise RuntimeError("Cannot reverse this migration. 'ChatDialog.user2' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ChatDialog.user2'
        db.add_column(u'np_server_chatdialog', 'user2',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['auth.User']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'ChatDialog.user1'
        raise RuntimeError("Cannot reverse this migration. 'ChatDialog.user1' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ChatDialog.user1'
        db.add_column(u'np_server_chatdialog', 'user1',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'ChatDialog.user'
        db.delete_column(u'np_server_chatdialog', 'user_id')

        # Deleting field 'ChatDialog.interlocutor'
        db.delete_column(u'np_server_chatdialog', 'interlocutor_id')


        # User chose to not deal with backwards NULL issues for 'ChatMessage.dialog'
        raise RuntimeError("Cannot reverse this migration. 'ChatMessage.dialog' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ChatMessage.dialog'
        db.add_column(u'np_server_chatmessage', 'dialog',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['np_server.ChatDialog']),
                      keep_default=False)


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
        u'np_server.chatdialog': {
            'Meta': {'ordering': "['-last_updated']", 'object_name': 'ChatDialog'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interlocutor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            'is_hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"})
        },
        u'np_server.chatmessage': {
            'Meta': {'ordering': "['add_time']", 'object_name': 'ChatMessage'},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'user_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            'user_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"})
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