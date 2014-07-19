from crispy_forms.utils import render_crispy_form
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView
import jsonview
from jsonview.decorators import json_view
from mainApp.models import *
from mainApp.forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from  mainApp import formH
import requests
from django.core import serializers
import json

def index(request) :
    return render(request,'home.html',{'sign_in_form':SignInForm})

#TRAIN
def train(request) :
    return render(request, 'train/train.html')

def exercises(request):
    exercises_obj = Exercise.objects.order_by('name')
    return render(request, 'train/exercises.html',{'items':exercises_obj})

def exercise(request,exercise_url):
    exercise_name = exercise_url.replace('_',' ')
    try:
        exercise_obj = Exercise.objects.get(name=exercise_name)
    except Exercise.DoesNotExist:
        print('exercise doesnt exists')
        return HttpResponseRedirect('/')

    return render(request, 'train/exercise.html',{'exercise':exercise_obj})


def workouts(request):
    items = Workout.objects.order_by('name')
    return render(request, 'train/workouts.html',{'items':items})

def workout (request, workout_url):
    workout_name = workout_url.replace('_',' ')
    try:
        workout_obj = Workout.objects.get(name=workout_name)
    except Workout.DoesNotExist:
        print('workout doesnt exists')
        return HttpResponseRedirect('/')

    days = WorkDay.objects.filter(workout=workout_obj)


    #try:
        #reviews = WorkoutReview.objects.filter(workout=workout_obj)
    """except WorkoutReview.DoesNotExist:
        print('reviews for the food doesnt exits')
        reviews = ''"""

    return render(request, 'train/workout.html',{'workout':workout_obj,'days':days})

def user_workouts(request):
    try:
        user_workouts_obj = UserWorkout.objects.filter(user = request.user)
    except UserWorkout.DoesNotExist:
        return HttpResponseRedirect('/')

    items = user_workouts_obj.values('workout')#_list('workout', flat=True).order_by('workout')
    print(items)

    return render(request, 'train/user_workouts.html',{'items':items})


#EAT
class Eat(ListView):
    model = Food
    context_object_name = 'foods'
    template_name = 'eat/eat.html'

def eat(request):
    items = Food.objects.order_by('name')
    return render(request,'eat/eat.html',{'items':items})

def food (request,food_url) :
    food_name = food_url.replace('_',' ')
    try:
        food_obj = Food.objects.get(name=food_name)
    except Food.DoesNotExist:
        print('food doesnt exists')
        return HttpResponseRedirect('/')

    ingredients = Ingredient.objects.filter(food=food_obj)
    reviews = FoodReview.objects.filter(food=food_obj).order_by('-time')


    return render(request, 'eat/food.html',{'food':food_obj,'reviews':reviews, 'ingredients':ingredients})


#SIGNING
def signUp(request) :

    signed_up = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        user_profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and user_profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = user_profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            signed_up = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(user_form.errors, user_profile_form.errors)
            print('not signed up')

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        user_profile_form = UserProfileForm()


    return render(request,'signUp.html',{'user_form':user_form,
                                         'user_profile_form':user_profile_form,
                                         'signed_up':signed_up})

def sign_in(request):
    return render(request,'sign_in.html',{'sign_in_form':SignInForm})

def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/')


#SUPPLY
def supplements(request):
    supplements_obj = Supply.objects.order_by('name')
    return render(request, 'supplements/supplements.html',{'items':supplements_obj})

def supply(request,supply_url):
    supply_name = supply_url.replace('_',' ')
    try:
       supply_obj = Supply.objects.get(name=supply_name)
    except Supply.DoesNotExist:
        print('supply doesnt exists')
        return HttpResponseRedirect('/supplements')

    return render(request, 'supplements/supply.html',{'supply':supply_obj})

def add_to_cart(request):
    supply_url = request.GET['supply_url']
    supply_name = supply_url.replace('_',' ')
    response = HttpResponse()

    if 'cart' in request.COOKIES:
        cart = request.COOKIES.get('cart')
        response.set_cookie('cart',str(cart) + ',' + supply_name)

    else:
        response.set_cookie('cart',supply_name)
    print('cart: ')
    print(request.COOKIES.get('cart'))
    return response

def cart(request):
    if request.COOKIES.get('cart'):
        cart_str = request.COOKIES.get('cart')
        cart_li = cart_str.split(',')
        return render(request,'supplements/cart.html',{'cart':cart_li})

    return render(request,'supplements/cart.html')


#CONTENT
@login_required
def add_content(request,name):
    form_for_name = {'food':FoodForm,
             'trainer':TrainerForm,
             'exercise':ExerciseForm,
             'workout':WorkoutForm
             }

    model_form = form_for_name[name]
    if not model_form:
        return HttpResponseRedirect('/')
    """
    if formH.was_sent(request,model_form):
        form = model_form(request.POST,request.FILES)
        form.save()
    """

    if request.method == 'POST':
        content_name = 'food'
        print('content name: ' + content_name)

        form_for_name = {'food':FoodForm,
             'trainer':TrainerForm,
             'exercise':ExerciseForm,
             'workout':WorkoutForm
             }

        model_form = form_for_name[content_name]
        print('model form reached')

        post = request.POST
        #post.pop('content_name')

        print('q dict reached ')

        form = model_form(data=post)
        if form.is_valid():
            print('form is valid')
            form.save()
            print('form saved')
            return HttpResponse(json.dumps({'saved':True}), content_type="application/json")

        form_html = render_crispy_form(form)
        print('form with errors:   ' + form_html)
        #return HttpResponse(json.dumps({'saved':False,'form':form_html}), content_type="application/json")

    return render(request,'add_content/add_content.html',{'form':model_form,'name':name})



def save_content(request):
    content_name = request.POST.get('content_name','')
    print('content name: ' + content_name)

    form_for_name = {'food':FoodForm,
             'trainer':TrainerForm,
             'exercise':ExerciseForm,
             'workout':WorkoutForm
             }

    model_form = form_for_name[content_name]
    print('model form reached')

    post = request.POST.copy()
    post.pop('content_name')

    print('q dict reached ')
    print('q urlencode reached')

    form = model_form(data=post)
    if form.is_valid():
        print('form is valid')
        form.save()
        print('form saved')
        return HttpResponse(json.dumps({'saved':True}), content_type="application/json")

    form_html = render_crispy_form(form)
    print('form with errors:   ' + form_html)
    return HttpResponse(json.dumps({'saved':False,'form':form_html}), content_type="application/json")



def get_list(request):
    model = request.GET['model']
    print(model)
    ord_by = request.GET['ord_by']
    print(ord_by)
    model_dic = {
        'food':Food,
    }
    if ord_by and model:
        obj_list = model_dic[model].objects.order_by(ord_by)
    else:
        obj_list = model_dic[model].objects.all()

    return render(request, 'cards.html',{'items':obj_list})

def search(request):
    model = request.GET['model']
    q = request.GET['q']

    print('q: ' + q + '   model: ' + model)

    model_dic = {
        'food':Food,
    }
    results_dic = {}
    Model = model_dic[model]
    words = q.split('_')
    print(words)
    #1`
    #for word in words:
    #    results = Model.objects.filter(name__contains=word)
    #    for result in results:
    #        if not results_dic[result.name]:
    #            results_dic[result.name] = 0
    #        else:
    #            results_dic[result.name] += 1
    #
    #    s_words = []
    #    for s_word in s_words:
    #
    #s_words = []
    #for i, word in words:
    #    s_words.append(requests.get('http://words.bighugelabs.com/api/2/056b5ac73f4132609cb896935fda5ecb/{0}/json'.format(word)))
    #    s_words[i] = serializers.deserialize('json', s_words[i])
    #print(s_words)
    #
    ##total_words = []
    ##for i,word in words:
    ##    total_words.append([word,s_words[i]])
    ###a_q =
    #for i, word in words:
    #    for s_word in s_words[i]:
    #        Model.objects.filter(name=q)

    return HttpResponse('hey')

def get_nutritional(request):
    food_name = request.GET['food']
    amount = request.GET['amount']

    try:
        food_obj = Food.objects.get(name=food_name)
    except Food.DoesNotExist:
        return HttpResponseRedirect('/')

    mult = float(amount)/100
    return render(request,'eat/nutritional.html',{'calories':food_obj.calories * mult,
                                                  'protein':food_obj.protein * mult,
                                                  'carbs':food_obj.carbs * mult,
                                                  'fat':food_obj.fat * mult})

#login action called via ajax

def login(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse('valid login')
        else:
            return HttpResponse('invalid login')
    else:
        return HttpResponse('invalid login')

class Forgot(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'forgot.html', {'forgot_form':ForgotFrom})


#Add Content
#-----------
class AddFood(CreateView):
    form_class = FoodForm
    template_name = 'add_content/add_food.html'

class AddExercise(CreateView):
    form_class = ExerciseForm
    template_name = 'add_content/add_exercise.html'


