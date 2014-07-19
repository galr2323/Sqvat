# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'WorkSession', fields ['exercise']
        db.delete_unique('mainApp_worksession', ['exercise_id'])


        # Changing field 'WorkSession.exercise'
        db.alter_column('mainApp_worksession', 'exercise_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainApp.Exercise']))

    def backwards(self, orm):

        # Changing field 'WorkSession.exercise'
        db.alter_column('mainApp_worksession', 'exercise_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['mainApp.Exercise']))
        # Adding unique constraint on 'WorkSession', fields ['exercise']
        db.create_unique('mainApp_worksession', ['exercise_id'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mainApp.brand': {
            'Meta': {'object_name': 'Brand'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'unique': 'True'})
        },
        'mainApp.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'muscles': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['mainApp.Muscle']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'unique': 'True'})
        },
        'mainApp.food': {
            'Meta': {'ordering': "['name']", 'object_name': 'Food'},
            'calories': ('django.db.models.fields.IntegerField', [], {}),
            'carbs': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'difficult_lvl': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'fat': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['mainApp.Ingredient']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'unique': 'True'}),
            'prep_time': ('django.db.models.fields.IntegerField', [], {}),
            'protein': ('django.db.models.fields.IntegerField', [], {})
        },
        'mainApp.foodreview': {
            'Meta': {'object_name': 'FoodReview', '_ormbases': ['mainApp.Review']},
            'food': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainApp.Food']"}),
            'review_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'unique': 'True', 'to': "orm['mainApp.Review']"})
        },
        'mainApp.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'unique': 'True'})
        },
        'mainApp.muscle': {
            'Meta': {'ordering': "['name']", 'object_name': 'Muscle'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'unique': 'True'})
        },
        'mainApp.review': {
            'Meta': {'object_name': 'Review'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'taste_rate': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainApp.UserProfile']"})
        },
        'mainApp.supply': {
            'Meta': {'object_name': 'Supply'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainApp.Brand']"}),
            'calories': ('django.db.models.fields.IntegerField', [], {}),
            'carbs': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'fat': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'unique': 'True'}),
            'protein': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['mainApp.SupplyType']"})
        },
        'mainApp.supplyreview': {
            'Meta': {'object_name': 'SupplyReview', '_ormbases': ['mainApp.Review']},
            'mix_rate': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'review_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'unique': 'True', 'to': "orm['mainApp.Review']"}),
            'supply': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainApp.Supply']"})
        },
        'mainApp.supplytype': {
            'Meta': {'object_name': 'SupplyType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'unique': 'True'})
        },
        'mainApp.trainer': {
            'Meta': {'object_name': 'Trainer'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'graduation': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['mainApp.UserProfile']"})
        },
        'mainApp.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'age': ('django.db.models.fields.DateField', [], {}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['auth.User']"})
        },
        'mainApp.userworkout': {
            'Meta': {'object_name': 'UserWorkout'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['mainApp.UserProfile']"}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainApp.Workout']"})
        },
        'mainApp.workday': {
            'Meta': {'object_name': 'WorkDay'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'sessions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['mainApp.WorkSession']"}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainApp.Workout']"})
        },
        'mainApp.workout': {
            'Meta': {'object_name': 'Workout'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'unique': 'True'}),
            'trainer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainApp.Trainer']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'mainApp.workoutreview': {
            'Meta': {'object_name': 'WorkoutReview', '_ormbases': ['mainApp.Review']},
            'review_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'unique': 'True', 'to': "orm['mainApp.Review']"}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainApp.Workout']"})
        },
        'mainApp.worksession': {
            'Meta': {'object_name': 'WorkSession'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainApp.Exercise']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reps': ('django.db.models.fields.IntegerField', [], {}),
            'rest': ('django.db.models.fields.FloatField', [], {}),
            'sets': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['mainApp']