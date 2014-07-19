from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model) :
    user = models.OneToOneField(User)

    age = models.DateField()

    GENDER_CHOICES = (
        ('m','Male'),
        ('f','Female')
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    """
    img = models.ImageField(upload_to='user_profile_imgs',blank=True)
    """
    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return 'user' + self.user.username


class Trainer (models.Model):
    #importing from user
    user = models.OneToOneField(UserProfile)

    #personal info
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='trainer_profile_imgs/')

    graduation = models.TextField()

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return 'user' + self.user.user.username

    def get_full_name(self):
        """returns the full trainers name"""
        return self.first_name + ' ' + self.last_name


class Muscle (models.Model):
    name = models.CharField(max_length=40,unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Exercise (models.Model):
    name = models.CharField(max_length=40,unique=True)

    description = models.TextField()

    #img = models.ImageField(upload_to='exercise_imgs')
    #video = models.FileField()
    muscles = models.ManyToManyField(Muscle)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/exercise/' + self.name.replace(' ','_')

class WorkSession(models.Model):
    exercise = models.ForeignKey(Exercise)
    sets = models.IntegerField()
    reps = models.IntegerField()
    rest = models.FloatField() #in minutes

    def __str__(self):
        return str(self.sets) + 'X' + str(self.reps) + ' ' + self.exercise.name

class Workout (models.Model):
    name = models.CharField(max_length=40,unique=True)

    trainer = models.ForeignKey(Trainer)

    TYPE_CHOICES = (
        ('general','General'),
        ('mass','Mass'),
        ('toning','Toning')
    )
    type = models.CharField(max_length=8, choices=TYPE_CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/workout/' + self.name.replace(' ','_')

class WorkDay(models.Model):
    workout = models.ForeignKey(Workout)
    num = models.IntegerField()
    sessions = models.ManyToManyField(WorkSession)

    def __str__(self):
        return self.workout.name + ' day ' + str(self.num)



class Ingredient (models.Model):
    #food = models.ForeignKey(Food)
    name = models.CharField(max_length=40, unique=True)
    img = models.ImageField(upload_to='ingredient_imgs')

    def __str__(self):
        return self.name


class Food (models.Model):
    name = models.CharField(max_length=40,unique=True)
    description = models.TextField()
    #img = models.ImageField(upload_to='food_img')
    ingredients = models.ManyToManyField(Ingredient)

    #nurtion in 100 grams
    calories = models.IntegerField()
    carbs = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()

    prep_time = models.IntegerField() #minutes

    LVL_CHOICES = (
        ('1','Child'),
        ('2','Beginner'),
        ('3','Average'),
        ('4','Pro')
    )
    difficult_lvl = models.CharField('difficult level',choices=LVL_CHOICES, max_length=8)

    class Meta():
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/food/' + str(self.name).replace(' ','_')



class Brand (models.Model):
    name = models.CharField(max_length=40,unique=True)
    img = models.ImageField(upload_to='brand_imgs')

    def __str__(self):
        return self.name

class SupplyType(models.Model):
    name = models.CharField(max_length=40,unique=True)

    def __str__(self):
        return self.name


class Supply(models.Model):
    name = models.CharField(max_length=40,unique=True)


    type = models.ForeignKey(SupplyType)
    brand = models.ForeignKey(Brand)
    description = models.TextField()

    #nurtion in 100 grams
    calories = models.IntegerField()
    carbs = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/supply/' + self.name.replace(' ', '_')

#REVIEWS
class Review (models.Model):
    user = models.ForeignKey(UserProfile)
    time = models.DateTimeField(auto_now_add=True)
    taste_rate = models.IntegerField(max_length=2)
    content = models.TextField()

class FoodReview (Review):
    food = models.ForeignKey(Food)

class SupplyReview (Review):
    supply = models.ForeignKey(Supply)
    mix_rate = models.IntegerField(max_length=2)

class WorkoutReview (Review):
    workout = models.ForeignKey(Workout)

class UserWorkout(models.Model):
    user = models.OneToOneField(UserProfile)
    workout = models.ForeignKey(Workout)

    def get_absolute_url(self):
        return self.workout.get_absolute_url()

class Cart(models.Model):
    user = models.OneToOneField(UserProfile)
    items = models.ManyToManyField(Supply)