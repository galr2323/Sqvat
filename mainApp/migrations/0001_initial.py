# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('mainApp_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('age', self.gf('django.db.models.fields.DateField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('mainApp', ['UserProfile'])

        # Adding model 'Trainer'
        db.create_table('mainApp_trainer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mainApp.UserProfile'], unique=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('graduation', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('mainApp', ['Trainer'])

        # Adding model 'Muscle'
        db.create_table('mainApp_muscle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40, unique=True)),
        ))
        db.send_create_signal('mainApp', ['Muscle'])

        # Adding model 'Exercise'
        db.create_table('mainApp_exercise', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40, unique=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('mainApp', ['Exercise'])

        # Adding M2M table for field muscles on 'Exercise'
        m2m_table_name = db.shorten_name('mainApp_exercise_muscles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('exercise', models.ForeignKey(orm['mainApp.exercise'], null=False)),
            ('muscle', models.ForeignKey(orm['mainApp.muscle'], null=False))
        ))
        db.create_unique(m2m_table_name, ['exercise_id', 'muscle_id'])

        # Adding model 'Workout'
        db.create_table('mainApp_workout', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40, unique=True)),
            ('trainer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainApp.Trainer'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('mainApp', ['Workout'])

        # Adding M2M table for field exercises on 'Workout'
        m2m_table_name = db.shorten_name('mainApp_workout_exercises')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workout', models.ForeignKey(orm['mainApp.workout'], null=False)),
            ('exercise', models.ForeignKey(orm['mainApp.exercise'], null=False))
        ))
        db.create_unique(m2m_table_name, ['workout_id', 'exercise_id'])

        # Adding model 'Ingredient'
        db.create_table('mainApp_ingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40, unique=True)),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('mainApp', ['Ingredient'])

        # Adding model 'Food'
        db.create_table('mainApp_food', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40, unique=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('calories', self.gf('django.db.models.fields.IntegerField')()),
            ('carbs', self.gf('django.db.models.fields.IntegerField')()),
            ('protein', self.gf('django.db.models.fields.IntegerField')()),
            ('fat', self.gf('django.db.models.fields.IntegerField')()),
            ('prep_time', self.gf('django.db.models.fields.IntegerField')()),
            ('difficult_lvl', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal('mainApp', ['Food'])

        # Adding M2M table for field ingredients on 'Food'
        m2m_table_name = db.shorten_name('mainApp_food_ingredients')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('food', models.ForeignKey(orm['mainApp.food'], null=False)),
            ('ingredient', models.ForeignKey(orm['mainApp.ingredient'], null=False))
        ))
        db.create_unique(m2m_table_name, ['food_id', 'ingredient_id'])

        # Adding model 'Brand'
        db.create_table('mainApp_brand', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40, unique=True)),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('mainApp', ['Brand'])

        # Adding model 'SupplyType'
        db.create_table('mainApp_supplytype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40, unique=True)),
        ))
        db.send_create_signal('mainApp', ['SupplyType'])

        # Adding model 'Supply'
        db.create_table('mainApp_supply', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40, unique=True)),
            ('type', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mainApp.SupplyType'], unique=True)),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainApp.Brand'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('calories', self.gf('django.db.models.fields.IntegerField')()),
            ('carbs', self.gf('django.db.models.fields.IntegerField')()),
            ('protein', self.gf('django.db.models.fields.IntegerField')()),
            ('fat', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('mainApp', ['Supply'])

        # Adding model 'Review'
        db.create_table('mainApp_review', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mainApp.UserProfile'], unique=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('taste_rate', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('mainApp', ['Review'])

        # Adding model 'FoodReview'
        db.create_table('mainApp_foodreview', (
            ('review_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, to=orm['mainApp.Review'], unique=True)),
            ('food', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainApp.Food'])),
        ))
        db.send_create_signal('mainApp', ['FoodReview'])

        # Adding model 'SupplyReview'
        db.create_table('mainApp_supplyreview', (
            ('review_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, to=orm['mainApp.Review'], unique=True)),
            ('supply', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainApp.Supply'])),
            ('mix_rate', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
        ))
        db.send_create_signal('mainApp', ['SupplyReview'])

        # Adding model 'WorkoutReview'
        db.create_table('mainApp_workoutreview', (
            ('review_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, to=orm['mainApp.Review'], unique=True)),
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainApp.Workout'])),
        ))
        db.send_create_signal('mainApp', ['WorkoutReview'])

        # Adding model 'UserWorkout'
        db.create_table('mainApp_userworkout', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mainApp.UserProfile'], unique=True)),
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainApp.Workout'])),
        ))
        db.send_create_signal('mainApp', ['UserWorkout'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('mainApp_userprofile')

        # Deleting model 'Trainer'
        db.delete_table('mainApp_trainer')

        # Deleting model 'Muscle'
        db.delete_table('mainApp_muscle')

        # Deleting model 'Exercise'
        db.delete_table('mainApp_exercise')

        # Removing M2M table for field muscles on 'Exercise'
        db.delete_table(db.shorten_name('mainApp_exercise_muscles'))

        # Deleting model 'Workout'
        db.delete_table('mainApp_workout')

        # Removing M2M table for field exercises on 'Workout'
        db.delete_table(db.shorten_name('mainApp_workout_exercises'))

        # Deleting model 'Ingredient'
        db.delete_table('mainApp_ingredient')

        # Deleting model 'Food'
        db.delete_table('mainApp_food')

        # Removing M2M table for field ingredients on 'Food'
        db.delete_table(db.shorten_name('mainApp_food_ingredients'))

        # Deleting model 'Brand'
        db.delete_table('mainApp_brand')

        # Deleting model 'SupplyType'
        db.delete_table('mainApp_supplytype')

        # Deleting model 'Supply'
        db.delete_table('mainApp_supply')

        # Deleting model 'Review'
        db.delete_table('mainApp_review')

        # Deleting model 'FoodReview'
        db.delete_table('mainApp_foodreview')

        # Deleting model 'SupplyReview'
        db.delete_table('mainApp_supplyreview')

        # Deleting model 'WorkoutReview'
        db.delete_table('mainApp_workoutreview')

        # Deleting model 'UserWorkout'
        db.delete_table('mainApp_userworkout')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Group']", 'blank': 'True', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)"},
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
            'Meta': {'object_name': 'Food', 'ordering': "['name']"},
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
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'taste_rate': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mainApp.UserProfile']", 'unique': 'True'})
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
            'exercises': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['mainApp.Exercise']"}),
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