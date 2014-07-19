from django import forms
from django.contrib.auth.models import User
from mainApp.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
#fix the import to only what needed

#USER
class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-7'

class UserProfileForm(forms.ModelForm):
    """
    img = forms.ImageField()
    age = forms.CharField(widget=forms.DateInput())
    GENDER_CHOICE = (
        ('m','male'),
        ('f','female')
    )
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices = GENDER_CHOICE)
    """

    nickName = forms.CharField(max_length=20)

    class Meta:
        model = UserProfile
        fields = ('nickName',)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-7'
        self.helper.add_input(Submit('submit', 'Submit'))

# Sign IN
class SignInForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(max_length=50)

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'sign-in-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-7'
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', 'Submit'))

#TRAIN

class TrainerForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    img = forms.ImageField()

    graduation = forms.CharField(max_length=40)

    class Meta:
        model = Trainer
        fields = ('first_name','last_name','img','graduation')

    def __init__(self, *args, **kwargs):
        super(TrainerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'trainer'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-7'
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', 'Submit'))

class ExerciseForm(forms.ModelForm):
    name = forms.CharField(max_length=40)

    class Meta:
        model = Exercise

    def __init__(self, *args, **kwargs):
        super(ExerciseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'exercise'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-7'
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', 'Submit'))

class WorkoutForm(forms.ModelForm):
    name = forms.CharField(max_length=20)
    #trainer
    description = forms.Textarea()
    #exercise

    class Meta:
        model = Workout

    def __init__(self, *args, **kwargs):
        super(WorkoutForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'workout'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-7'
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', 'Submit'))


#EAT
class FoodForm(forms.ModelForm):
    name = forms.CharField(max_length=40)
    description = forms.Textarea()
    #img field needed ------------
    ingredients = forms.ModelMultipleChoiceField(Ingredient.objects.order_by('name'))

    calories = forms.IntegerField()
    carbs = forms.IntegerField()
    protein = forms.IntegerField()
    fat = forms.IntegerField()

    prep_time = forms.IntegerField()
    difficult_lvl = forms.ChoiceField(choices=Food.LVL_CHOICES)


    class Meta:
        model = Food
        fields = ('name','calories','carbs','protein','fat','prep_time','description','ingredients')

    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'food'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-7'
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', 'Submit'))

#SUPPLY

#STORE

#class ReviewForm(forms.ModelForm):

class FoodReviewForm(forms.ModelForm):

    class Meta:
        model = FoodReview

class ForgotFrom(forms.Form):
    email = forms.EmailField()

    class Meta:
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super(ForgotFrom, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-7'

        self.helper.add_input(Submit('submit', 'Submit'))
