# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Review', fields ['user']
        db.delete_unique('mainApp_review', ['user_id'])

        # Deleting field 'Review.date'
        db.delete_column('mainApp_review', 'date')

        # Adding field 'Review.time'
        db.add_column('mainApp_review', 'time',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True, default=datetime.datetime(2014, 6, 24, 0, 0)),
                      keep_default=False)


        # Changing field 'Review.user'
        db.alter_column('mainApp_review', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainApp.UserProfile']))

    def backwards(self, orm):
        # Adding field 'Review.date'
        db.add_column('mainApp_review', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 6, 24, 0, 0)),
                      keep_default=False)

        # Deleting field 'Review.time'
        db.delete_column('mainApp_review', 'time')


        # Changing field 'Review.user'
        db.alter_column('mainApp_review', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mainApp.UserProfile'], unique=True))
        # Adding unique constraint on 'Review', fields ['user']
        db.create_unique('mainApp_review', ['user_id'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Group']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'", 'ordering': "('name',)"},
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
            'muscles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mainApp.Muscle']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'unique': 'True'})
        },
        'mainApp.food': {
            'Meta': {'object_name': 'Food', 'ordering': "['name']"},
            'calories': ('django.db.models.fields.IntegerField', [], {}),
            'carbs': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'difficult_lvl': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'fat': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mainApp.Ingredient']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'unique': 'True'}),
            'prep_time': ('django.db.models.fields.IntegerField', [], {}),
            'protein': ('django.db.models.fields.IntegerField', [], {})
        },
        'mainApp.foodreview': {
            'Meta': {'object_name': 'FoodReview', '_ormbases': ['mainApp.Review']},
            'food': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainApp.Food']"}),
            'review_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'to': "orm['mainApp.Review']", 'unique': 'True'})
        },
        'mainApp.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'unique': 'True'})
        },
        'mainApp.muscle': {
            'Meta': {'object_name': 'Muscle', 'ordering': "['name']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'unique': 'True'})
        },
        'mainApp.review': {
            'Meta': {'object_name': 'Review'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'taste_rate': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
            'type': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mainApp.SupplyType']", 'unique': 'True'})
        },
        'mainApp.supplyreview': {
            'Meta': {'object_name': 'SupplyReview', '_ormbases': ['mainApp.Review']},
            'mix_rate': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'review_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'to': "orm['mainApp.Review']", 'unique': 'True'}),
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
            'graduation': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mainApp.UserProfile']", 'unique': 'True'})
        },
        'mainApp.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'age': ('django.db.models.fields.DateField', [], {}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'mainApp.userworkout': {
            'Meta': {'object_name': 'UserWorkout'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mainApp.UserProfile']", 'unique': 'True'}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainApp.Workout']"})
        },
        'mainApp.workout': {
            'Meta': {'object_name': 'Workout'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'exercises': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mainApp.Exercise']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'unique': 'True'}),
            'trainer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainApp.Trainer']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'mainApp.workoutreview': {
            'Meta': {'object_name': 'WorkoutReview', '_ormbases': ['mainApp.Review']},
            'review_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'to': "orm['mainApp.Review']", 'unique': 'True'}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainApp.Workout']"})
        }
    }

    complete_apps = ['mainApp']