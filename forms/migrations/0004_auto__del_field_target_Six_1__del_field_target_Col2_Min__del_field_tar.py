# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Target.Six_1'
        db.delete_column('forms_target', 'Six_1')

        # Deleting field 'Target.Col2_Min'
        db.delete_column('forms_target', 'Col2_Min')

        # Deleting field 'Target.Col2_Oth'
        db.delete_column('forms_target', 'Col2_Oth')

        # Deleting field 'Target.Col6_PWD'
        db.delete_column('forms_target', 'Col6_PWD')

        # Deleting field 'Target.Col3_Min'
        db.delete_column('forms_target', 'Col3_Min')

        # Deleting field 'Target.Col3_Oth'
        db.delete_column('forms_target', 'Col3_Oth')

        # Deleting field 'Target.Four_6'
        db.delete_column('forms_target', 'Four_6')

        # Deleting field 'Target.Four_5'
        db.delete_column('forms_target', 'Four_5')

        # Deleting field 'Target.Four_4'
        db.delete_column('forms_target', 'Four_4')

        # Deleting field 'Target.Four_3'
        db.delete_column('forms_target', 'Four_3')

        # Deleting field 'Target.Col2_ST'
        db.delete_column('forms_target', 'Col2_ST')

        # Deleting field 'Target.Col6_Min'
        db.delete_column('forms_target', 'Col6_Min')

        # Deleting field 'Target.Col3_ST'
        db.delete_column('forms_target', 'Col3_ST')

        # Deleting field 'Target.Five_2'
        db.delete_column('forms_target', 'Five_2')

        # Deleting field 'Target.Five_1'
        db.delete_column('forms_target', 'Five_1')

        # Deleting field 'Target.Col6_SC'
        db.delete_column('forms_target', 'Col6_SC')

        # Deleting field 'Target.Col6_ST'
        db.delete_column('forms_target', 'Col6_ST')

        # Deleting field 'Target.Col3_SC'
        db.delete_column('forms_target', 'Col3_SC')

        # Deleting field 'Target.Col2_PWD'
        db.delete_column('forms_target', 'Col2_PWD')

        # Deleting field 'Target.Col3_PWD'
        db.delete_column('forms_target', 'Col3_PWD')

        # Deleting field 'Target.Col6_Oth'
        db.delete_column('forms_target', 'Col6_Oth')

        # Deleting field 'Target.Col2_SC'
        db.delete_column('forms_target', 'Col2_SC')


    def backwards(self, orm):
        # Adding field 'Target.Six_1'
        db.add_column('forms_target', 'Six_1',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Target.Col2_Min'
        db.add_column('forms_target', 'Col2_Min',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Target.Col2_Oth'
        db.add_column('forms_target', 'Col2_Oth',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Target.Col6_PWD'
        db.add_column('forms_target', 'Col6_PWD',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Target.Col3_Min'
        db.add_column('forms_target', 'Col3_Min',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Target.Col3_Oth'
        db.add_column('forms_target', 'Col3_Oth',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Target.Four_6'
        db.add_column('forms_target', 'Four_6',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Target.Four_5'
        db.add_column('forms_target', 'Four_5',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Target.Four_4'
        db.add_column('forms_target', 'Four_4',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Target.Four_3'
        db.add_column('forms_target', 'Four_3',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Target.Col2_ST'
        db.add_column('forms_target', 'Col2_ST',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Target.Col6_Min'
        db.add_column('forms_target', 'Col6_Min',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Target.Col3_ST'
        db.add_column('forms_target', 'Col3_ST',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Target.Five_2'
        db.add_column('forms_target', 'Five_2',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Target.Five_1'
        db.add_column('forms_target', 'Five_1',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Target.Col6_SC'
        db.add_column('forms_target', 'Col6_SC',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Target.Col6_ST'
        db.add_column('forms_target', 'Col6_ST',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Target.Col3_SC'
        db.add_column('forms_target', 'Col3_SC',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Target.Col2_PWD'
        db.add_column('forms_target', 'Col2_PWD',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Target.Col3_PWD'
        db.add_column('forms_target', 'Col3_PWD',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Target.Col6_Oth'
        db.add_column('forms_target', 'Col6_Oth',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Target.Col2_SC'
        db.add_column('forms_target', 'Col2_SC',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'forms.cocouser': {
            'Meta': {'object_name': 'CocoUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'states': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['forms.State']", 'symmetrical': 'False'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cocouser_created'", 'null': 'True', 'to': "orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cocouser_related_modified'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'forms.financialassistance': {
            'Col2_Min': ('django.db.models.fields.IntegerField', [], {}),
            'Col2_Oth': ('django.db.models.fields.IntegerField', [], {}),
            'Col2_PWD': ('django.db.models.fields.IntegerField', [], {}),
            'Col2_SC': ('django.db.models.fields.IntegerField', [], {}),
            'Col2_ST': ('django.db.models.fields.IntegerField', [], {}),
            'Col3_Min': ('django.db.models.fields.IntegerField', [], {}),
            'Col3_Oth': ('django.db.models.fields.IntegerField', [], {}),
            'Col3_PWD': ('django.db.models.fields.IntegerField', [], {}),
            'Col3_SC': ('django.db.models.fields.IntegerField', [], {}),
            'Col3_ST': ('django.db.models.fields.IntegerField', [], {}),
            'Col4_Min': ('django.db.models.fields.IntegerField', [], {}),
            'Col4_Oth': ('django.db.models.fields.IntegerField', [], {}),
            'Col4_PWD': ('django.db.models.fields.IntegerField', [], {}),
            'Col4_SC': ('django.db.models.fields.IntegerField', [], {}),
            'Col4_ST': ('django.db.models.fields.IntegerField', [], {}),
            'Col5_Min': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Col5_Oth': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Col5_PWD': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Col5_SC': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Col5_ST': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Col6_Min': ('django.db.models.fields.IntegerField', [], {}),
            'Col6_Oth': ('django.db.models.fields.IntegerField', [], {}),
            'Col6_PWD': ('django.db.models.fields.IntegerField', [], {}),
            'Col6_SC': ('django.db.models.fields.IntegerField', [], {}),
            'Col6_ST': ('django.db.models.fields.IntegerField', [], {}),
            'Col7_Min': ('django.db.models.fields.IntegerField', [], {}),
            'Col7_Oth': ('django.db.models.fields.IntegerField', [], {}),
            'Col7_PWD': ('django.db.models.fields.IntegerField', [], {}),
            'Col7_SC': ('django.db.models.fields.IntegerField', [], {}),
            'Col7_ST': ('django.db.models.fields.IntegerField', [], {}),
            'Col8_Min': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Col8_Oth': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Col8_PWD': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Col8_SC': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Col8_ST': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Meta': {'object_name': 'FinancialAssistance'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "'Month'"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forms.Project']"}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forms.State']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'financialassistance_created'", 'null': 'True', 'to': "orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'financialassistance_related_modified'", 'null': 'True', 'to': "orm['auth.User']"}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'forms.fulldownloadstats': {
            'Meta': {'object_name': 'FullDownloadStats'},
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'forms.hrdetails': {
            'Col2_bmmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col2_bmmup': ('django.db.models.fields.IntegerField', [], {}),
            'Col2_dmmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col2_smmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col3_bmmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col3_bmmup': ('django.db.models.fields.IntegerField', [], {}),
            'Col3_dmmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col3_smmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col4_bmmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col4_bmmup': ('django.db.models.fields.IntegerField', [], {}),
            'Col4_dmmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col4_smmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col5_bmmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col5_bmmup': ('django.db.models.fields.IntegerField', [], {}),
            'Col5_dmmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col5_smmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col6_bmmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col6_bmmup': ('django.db.models.fields.IntegerField', [], {}),
            'Col6_dmmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col6_smmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col7_bmmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col7_bmmup': ('django.db.models.fields.IntegerField', [], {}),
            'Col7_dmmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col7_smmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col8_bmmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col8_bmmup': ('django.db.models.fields.IntegerField', [], {}),
            'Col8_dmmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col8_smmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col9_bmmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col9_bmmup': ('django.db.models.fields.IntegerField', [], {}),
            'Col9_dmmu': ('django.db.models.fields.IntegerField', [], {}),
            'Col9_smmu': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'HrDetails'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "'Month'"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forms.Project']"}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forms.State']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'hrdetails_created'", 'null': 'True', 'to': "orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'hrdetails_related_modified'", 'null': 'True', 'to': "orm['auth.User']"}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'forms.progress': {
            'Five_1': ('django.db.models.fields.IntegerField', [], {}),
            'Five_10': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Five_11': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Five_12': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Five_13': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Five_14': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Five_2': ('django.db.models.fields.IntegerField', [], {}),
            'Five_5': ('django.db.models.fields.IntegerField', [], {}),
            'Five_6': ('django.db.models.fields.IntegerField', [], {}),
            'Five_7': ('django.db.models.fields.IntegerField', [], {}),
            'Five_8': ('django.db.models.fields.IntegerField', [], {}),
            'Five_9': ('django.db.models.fields.IntegerField', [], {}),
            'Four_1': ('django.db.models.fields.IntegerField', [], {}),
            'Four_2': ('django.db.models.fields.IntegerField', [], {}),
            'Four_3': ('django.db.models.fields.IntegerField', [], {}),
            'Four_4': ('django.db.models.fields.IntegerField', [], {}),
            'Four_5': ('django.db.models.fields.IntegerField', [], {}),
            'Four_6': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'Progress'},
            'Seven_1': ('django.db.models.fields.IntegerField', [], {}),
            'Seven_2': ('django.db.models.fields.IntegerField', [], {}),
            'Seven_3': ('django.db.models.fields.IntegerField', [], {}),
            'Seven_4': ('django.db.models.fields.IntegerField', [], {}),
            'Seven_5': ('django.db.models.fields.IntegerField', [], {}),
            'Seven_6': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Seven_7': ('django.db.models.fields.IntegerField', [], {}),
            'Seven_8': ('django.db.models.fields.IntegerField', [], {}),
            'Seven_9': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Six_1': ('django.db.models.fields.IntegerField', [], {}),
            'Six_10': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Six_11': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Six_12': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Six_13': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Six_14': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Six_2': ('django.db.models.fields.IntegerField', [], {}),
            'Six_5': ('django.db.models.fields.IntegerField', [], {}),
            'Six_6': ('django.db.models.fields.IntegerField', [], {}),
            'Six_7': ('django.db.models.fields.IntegerField', [], {}),
            'Six_8': ('django.db.models.fields.IntegerField', [], {}),
            'Six_9': ('django.db.models.fields.IntegerField', [], {}),
            'Three_1': ('django.db.models.fields.IntegerField', [], {}),
            'Three_2': ('django.db.models.fields.IntegerField', [], {}),
            'Three_4': ('django.db.models.fields.IntegerField', [], {}),
            'Three_5': ('django.db.models.fields.IntegerField', [], {}),
            'Three_6': ('django.db.models.fields.IntegerField', [], {}),
            'Three_7': ('django.db.models.fields.IntegerField', [], {}),
            'Three_8': ('django.db.models.fields.IntegerField', [], {}),
            'Two_1': ('django.db.models.fields.IntegerField', [], {}),
            'Two_2': ('django.db.models.fields.IntegerField', [], {}),
            'Two_3': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "'Month'"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forms.Project']"}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forms.State']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'progress_created'", 'null': 'True', 'to': "orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'progress_related_modified'", 'null': 'True', 'to': "orm['auth.User']"}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'forms.progresstill13': {
            'Five_1': ('django.db.models.fields.IntegerField', [], {}),
            'Five_10': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Five_11': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Five_12': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Five_13': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Five_14': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Five_2': ('django.db.models.fields.IntegerField', [], {}),
            'Five_5': ('django.db.models.fields.IntegerField', [], {}),
            'Five_6': ('django.db.models.fields.IntegerField', [], {}),
            'Five_7': ('django.db.models.fields.IntegerField', [], {}),
            'Five_8': ('django.db.models.fields.IntegerField', [], {}),
            'Five_9': ('django.db.models.fields.IntegerField', [], {}),
            'Four_1': ('django.db.models.fields.IntegerField', [], {}),
            'Four_2': ('django.db.models.fields.IntegerField', [], {}),
            'Four_3': ('django.db.models.fields.IntegerField', [], {}),
            'Four_4': ('django.db.models.fields.IntegerField', [], {}),
            'Four_5': ('django.db.models.fields.IntegerField', [], {}),
            'Four_6': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'ProgressTill13'},
            'Seven_1': ('django.db.models.fields.IntegerField', [], {}),
            'Seven_2': ('django.db.models.fields.IntegerField', [], {}),
            'Seven_3': ('django.db.models.fields.IntegerField', [], {}),
            'Seven_4': ('django.db.models.fields.IntegerField', [], {}),
            'Seven_5': ('django.db.models.fields.IntegerField', [], {}),
            'Seven_6': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Seven_7': ('django.db.models.fields.IntegerField', [], {}),
            'Seven_8': ('django.db.models.fields.IntegerField', [], {}),
            'Seven_9': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Six_1': ('django.db.models.fields.IntegerField', [], {}),
            'Six_10': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Six_11': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Six_12': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Six_13': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Six_14': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Six_2': ('django.db.models.fields.IntegerField', [], {}),
            'Six_5': ('django.db.models.fields.IntegerField', [], {}),
            'Six_6': ('django.db.models.fields.IntegerField', [], {}),
            'Six_7': ('django.db.models.fields.IntegerField', [], {}),
            'Six_8': ('django.db.models.fields.IntegerField', [], {}),
            'Six_9': ('django.db.models.fields.IntegerField', [], {}),
            'Three_1': ('django.db.models.fields.IntegerField', [], {}),
            'Three_2': ('django.db.models.fields.IntegerField', [], {}),
            'Three_4': ('django.db.models.fields.IntegerField', [], {}),
            'Three_5': ('django.db.models.fields.IntegerField', [], {}),
            'Three_6': ('django.db.models.fields.IntegerField', [], {}),
            'Three_7': ('django.db.models.fields.IntegerField', [], {}),
            'Three_8': ('django.db.models.fields.IntegerField', [], {}),
            'Two_1': ('django.db.models.fields.IntegerField', [], {}),
            'Two_2': ('django.db.models.fields.IntegerField', [], {}),
            'Two_3': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "'Month'"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forms.Project']"}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forms.State']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'progresstill13_created'", 'null': 'True', 'to': "orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'progresstill13_related_modified'", 'null': 'True', 'to': "orm['auth.User']"}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'forms.project': {
            'Meta': {'object_name': 'Project'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30', 'db_column': "'PROJECT_NAME'"})
        },
        'forms.serverlog': {
            'Meta': {'object_name': 'ServerLog'},
            'action': ('django.db.models.fields.IntegerField', [], {}),
            'entry_table': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
        },
        'forms.state': {
            'Meta': {'object_name': 'State'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30', 'db_column': "'STATE_NAME'"})
        },
        'forms.target': {
            'Col4_Min': ('django.db.models.fields.IntegerField', [], {}),
            'Col4_Oth': ('django.db.models.fields.IntegerField', [], {}),
            'Col4_PWD': ('django.db.models.fields.IntegerField', [], {}),
            'Col4_SC': ('django.db.models.fields.IntegerField', [], {}),
            'Col4_ST': ('django.db.models.fields.IntegerField', [], {}),
            'Col5_Min': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Col5_Oth': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Col5_PWD': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Col5_SC': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Col5_ST': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Col7_Min': ('django.db.models.fields.IntegerField', [], {}),
            'Col7_Oth': ('django.db.models.fields.IntegerField', [], {}),
            'Col7_PWD': ('django.db.models.fields.IntegerField', [], {}),
            'Col7_SC': ('django.db.models.fields.IntegerField', [], {}),
            'Col7_ST': ('django.db.models.fields.IntegerField', [], {}),
            'Col8_Min': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Col8_Oth': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Col8_PWD': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Col8_SC': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Col8_ST': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Five_10': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Five_11': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Five_12': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Five_13': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Five_14': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Five_5': ('django.db.models.fields.IntegerField', [], {}),
            'Five_6': ('django.db.models.fields.IntegerField', [], {}),
            'Five_7': ('django.db.models.fields.IntegerField', [], {}),
            'Five_8': ('django.db.models.fields.IntegerField', [], {}),
            'Five_9': ('django.db.models.fields.IntegerField', [], {}),
            'Four_1': ('django.db.models.fields.IntegerField', [], {}),
            'Four_2': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'Target'},
            'Seven_1': ('django.db.models.fields.IntegerField', [], {}),
            'Seven_2': ('django.db.models.fields.IntegerField', [], {}),
            'Seven_3': ('django.db.models.fields.IntegerField', [], {}),
            'Seven_4': ('django.db.models.fields.IntegerField', [], {}),
            'Seven_5': ('django.db.models.fields.IntegerField', [], {}),
            'Seven_6': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Seven_7': ('django.db.models.fields.IntegerField', [], {}),
            'Seven_8': ('django.db.models.fields.IntegerField', [], {}),
            'Seven_9': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Six_10': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Six_11': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Six_12': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Six_13': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Six_14': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'Six_2': ('django.db.models.fields.IntegerField', [], {}),
            'Six_5': ('django.db.models.fields.IntegerField', [], {}),
            'Six_6': ('django.db.models.fields.IntegerField', [], {}),
            'Six_7': ('django.db.models.fields.IntegerField', [], {}),
            'Six_8': ('django.db.models.fields.IntegerField', [], {}),
            'Six_9': ('django.db.models.fields.IntegerField', [], {}),
            'Three_1': ('django.db.models.fields.IntegerField', [], {}),
            'Three_2': ('django.db.models.fields.IntegerField', [], {}),
            'Three_4': ('django.db.models.fields.IntegerField', [], {}),
            'Three_5': ('django.db.models.fields.IntegerField', [], {}),
            'Three_6': ('django.db.models.fields.IntegerField', [], {}),
            'Three_7': ('django.db.models.fields.IntegerField', [], {}),
            'Three_8': ('django.db.models.fields.IntegerField', [], {}),
            'Two_1': ('django.db.models.fields.IntegerField', [], {}),
            'Two_2': ('django.db.models.fields.IntegerField', [], {}),
            'Two_3': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forms.Project']"}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['forms.State']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'target_created'", 'null': 'True', 'to': "orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'target_related_modified'", 'null': 'True', 'to': "orm['auth.User']"}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        }
    }

    complete_apps = ['forms']