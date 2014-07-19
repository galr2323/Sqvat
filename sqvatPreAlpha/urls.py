from django.conf.urls import patterns, include, url
from mainApp.views import *
from django.contrib import admin
admin.autodiscover()




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sqvatPreAlpha.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^signUp/$', signUp),
     url(r'^sign_in/$', 'mainApp.views.sign_in'),
    url(r'^sign_out/$', 'mainApp.views.sign_out'),

    url(r'^train/$', 'mainApp.views.train'),

    url(r'^exercises/$', 'mainApp.views.exercises'),
    url(r'^exercise/(?P<exercise_url>\w+)/$', exercise),

    url(r'^workouts/$', workouts),
    url(r'^workout/(?P<workout_url>\w+)/$', workout),

    url(r'^user_workouts/$', user_workouts),

    url(r'^eat/$', eat),
    url(r'^food/(?P<food_url>\w+)/$', food),

    url(r'^supplements/$', 'mainApp.views.supplements'),
    url(r'^supply/(?P<supply_url>\w+)/$', 'mainApp.views.supply'),
    url(r'^add_to_cart/$', 'mainApp.views.add_to_cart'),
    url(r'^cart/$', 'mainApp.views.cart'),


    url(r'^add_content/(?P<name>\w+)$', 'mainApp.views.add_content'),
    url(r'^add_food/$', AddFood.as_view()),
    url(r'^add_exercise/$', AddExercise.as_view()),

    url(r'^get_list/$', get_list),
    url(r'^search/$', search),
    url(r'^get_nutritional/$', get_nutritional),
    url(r'^save_content/$', save_content),
    url(r'^login/$', login),
    url(r'^forgot/$', Forgot.as_view()),



)
