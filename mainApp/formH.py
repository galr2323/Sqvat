from django.contrib.auth import authenticate
from django.shortcuts import render
from mainApp.models import *
from mainApp.forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

def was_sent (request,Form):
    if request.method == 'POST':
        form = Form(data=request.POST)
        if form.is_valid():
            return True
        else:
            print(form.errors)
            print('form isnt vaild')


    return False
