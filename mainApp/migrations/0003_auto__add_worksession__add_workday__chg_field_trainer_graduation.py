# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WorkSession'
        db.create_table('mainApp_worksession', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainApp.Exercise'])),
            ('sets', self.gf('django.db.models.fields.IntegerField')()),
            ('reps', self.gf('django.db.models.fields.IntegerField')()),
            ('rest', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('mainApp', ['WorkSession'])

        # Adding model 'WorkDay'
        db.create_table('mainApp_workday', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainApp.Workout'])),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('mainApp', ['WorkDay'])

        # Adding M2M table for field sessions on 'WorkDay'
        m2m_table_name = db.shorten_name('mainApp_workday_sessions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workday', models.ForeignKey(orm['mainApp.workday'], null=False)),
            ('worksession', models.ForeignKey(orm['mainApp.worksession'], null=False))
        ))
        db.create_unique(m2m_table_name, ['workday_id', 'worksession_id'])

        # Removing M2M table for field exercises on 'Workout'
        db.delete_table(db.shorten_name('mainApp_workout_exercises'))


        # Changing field 'Trainer.graduation'
        db.alter_column('mainApp_trainer', 'graduation', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Deleting model 'WorkSession'
        db.delete_table('mainApp_worksession')

        # Deleting model 'WorkDay'
        db.delete_table('mainApp_workday')

        # Removing M2M table for field sessions on 'WorkDay'
        db.delete_table(db.shorten_name('mainApp_workday_sessions'))

        # Adding M2M table for field exercises on 'Workout'
        m2m_table_name = db.shorten_name('mainApp_workout_exercises')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workout', models.ForeignKey(orm['mainApp.workout'], null=False)),
            ('exercise', models.ForeignKey(orm['mainApp.exercise'], null=False))
        ))
        db.create_unique(m2m_table_name, ['workout_id', 'exercise_id'])


        # Changing field 'Trainer.graduation'
        db.alter_column('mainApp_trainer', 'graduation', self.gf('django.db.models.fields.CharField')(max_length=40))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
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
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mainApp.brand': {
            'Meta': {'object_name': 'Brand'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'})
        },
        'mainApp.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'muscles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mainApp.Muscle']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'})
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
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mainApp.Ingredient']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'prep_time': ('django.db.models.fields.IntegerField', [], {}),
            'protein': ('django.db.models.fields.IntegerField', [], {})
        },
        'mainApp.foodreview': {
            'Meta': {'_ormbases': ['mainApp.Review'], 'object_name': 'FoodReview'},
            'food': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainApp.Food']"}),
            'review_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['mainApp.Review']", 'primary_key': 'True'})
        },
        'mainApp.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'})
        },
        'mainApp.muscle': {
            'Meta': {'ordering': "['name']", 'object_name': 'Muscle'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'})
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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'protein': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['mainApp.SupplyType']"})
        },
        'mainApp.supplyreview': {
            'Meta': {'_ormbases': ['mainApp.Review'], 'object_name': 'SupplyReview'},
            'mix_rate': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'review_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['mainApp.Review']", 'primary_key': 'True'}),
            'supply': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainApp.Supply']"})
        },
        'mainApp.supplytype': {
            'Meta': {'object_name': 'SupplyType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'})
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
            'sessions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mainApp.WorkSession']", 'symmetrical': 'False'}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainApp.Workout']"})
        },
        'mainApp.workout': {
            'Meta': {'object_name': 'Workout'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'trainer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainApp.Trainer']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'mainApp.workoutreview': {
            'Meta': {'_ormbases': ['mainApp.Review'], 'object_name': 'WorkoutReview'},
            'review_ptr': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['mainApp.Review']", 'primary_key': 'True'}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainApp.Workout']"})
        },
        'mainApp.worksession': {
            'Meta': {'object_name': 'WorkSession'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainApp.Exercise']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reps': ('django.db.models.fields.IntegerField', [], {}),
            'rest': ('django.db.models.fields.IntegerField', [], {}),
            'sets': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['mainApp']