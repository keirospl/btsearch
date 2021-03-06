# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        mapping = {
            '1': 'DLN',
            '2': 'KPM',
            '3': 'LUB',
            '4': 'LBS',
            '5': 'LDZ',
            '6': 'MLP',
            '7': 'MAZ',
            '8': 'OPO',
            '9': 'PDK',
            '10': 'PDL',
            '11': 'POM',
            '12': 'SLK',
            '13': 'SWK',
            '14': 'WMZ',
            '15': 'WLK',
            '16': 'ZPM'
        }
        for region in orm['bts.Region'].objects.all():
            reg_id = str(region.id)
            region.code = mapping.get(reg_id)
            region.save()

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'bts.basestation': {
            'Meta': {'object_name': 'BaseStation'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'edit_status': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'enbi': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
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
            'rnc': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'station_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '16', 'blank': 'True'}),
            'station_status': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'bts.basestationpermission': {
            'Meta': {'unique_together': "(['base_station', 'permission', 'station_id'],)", 'object_name': 'BaseStationPermission'},
            'base_station': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'permissions'", 'to': u"orm['bts.BaseStation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'permission': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'base_stations'", 'to': u"orm['uke.Permission']"}),
            'station_id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'db_index': 'True'})
        },
        u'bts.cell': {
            'Meta': {'object_name': 'Cell'},
            'azimuth': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'band': ('django.db.models.fields.CharField', [], {'max_length': '8', 'db_index': 'True'}),
            'base_station': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cells'", 'to': u"orm['bts.BaseStation']"}),
            'cid': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'cid_long': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_ping': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'ecid': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lac': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'standard': ('django.db.models.fields.CharField', [], {'max_length': '8', 'db_index': 'True'}),
            'ua_freq': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
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
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'uke.location': {
            'Meta': {'ordering': "['id']", 'object_name': 'Location'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '6', 'db_index': 'True'}),
            'latitude_uke': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'location_hash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32', 'db_index': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '6', 'db_index': 'True'}),
            'longitude_uke': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        u'uke.operator': {
            'Meta': {'object_name': 'Operator'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'uke_operators'", 'to': u"orm['bts.Network']"}),
            'operator_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        u'uke.permission': {
            'Meta': {'object_name': 'Permission'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'band': ('django.db.models.fields.CharField', [], {'max_length': '16', 'db_index': 'True'}),
            'case_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64', 'db_index': 'True'}),
            'case_number_orig': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'case_type': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'permissions'", 'to': u"orm['uke.Location']"}),
            'network': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'permissions'", 'null': 'True', 'to': u"orm['bts.Network']"}),
            'operator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'permissions'", 'to': u"orm['uke.Operator']"}),
            'standard': ('django.db.models.fields.CharField', [], {'max_length': '16', 'db_index': 'True'}),
            'station_id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'db_index': 'True'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['bts']
    symmetrical = True
