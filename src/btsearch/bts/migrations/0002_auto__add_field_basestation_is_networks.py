# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BaseStation.is_networks'
        db.add_column(u'bts_basestation', 'is_networks',
                      self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BaseStation.is_networks'
        db.delete_column(u'bts_basestation', 'is_networks')


    models = {
        u'bts.basestation': {
            'Meta': {'object_name': 'BaseStation'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'edit_status': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_cdma': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_common_bcch': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_gsm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_lte': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_networks': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'is_umts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'base_stations'", 'to': u"orm['bts.Location']"}),
            'location_details': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'network': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'base_stations'", 'to': u"orm['bts.Network']"}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'rnc': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'station_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '16', 'blank': 'True'}),
            'station_status': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'bts.cell': {
            'Meta': {'object_name': 'Cell'},
            'azimuth': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'band': ('django.db.models.fields.CharField', [], {'max_length': '8', 'db_index': 'True'}),
            'base_station': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cells'", 'to': u"orm['bts.BaseStation']"}),
            'cid': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'cid_long': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_ping': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lac': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'standard': ('django.db.models.fields.CharField', [], {'max_length': '8', 'db_index': 'True'}),
            'ua_freq': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'bts.location': {
            'Meta': {'ordering': "['town']", 'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '6', 'db_index': 'True'}),
            'location_hash': ('django.db.models.fields.CharField', [], {'max_length': '32', 'db_index': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '6', 'db_index': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locations'", 'to': u"orm['bts.Region']"}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'bts.network': {
            'Meta': {'ordering': "['code']", 'object_name': 'Network'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True'}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'operator_name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'bts.region': {
            'Meta': {'object_name': 'Region'},
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['bts']