import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.forms import inlineformset_factory

from .forms import *


nowaday = datetime.date.today()

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def dashboard(request):
    username = request.session.get('username')
    return render(request, 'dashboard.html', {'username': username})

@login_required
def profile(request):
    username = request.session.get('username')
    user = User.objects.get(username__exact=username)
    age = nowaday.year - user.profilebasic.dob.year

    if request.method == 'POST':
        if userbase.is_valid():
            userforms = UserForm(request.POST, instance=user)
            probases = UserProBaseInline(request.POST, request.FILES, instance=user)
            userbase.save()

    else:
        userforms = UserForm(instance=user)
        probases = UserProBaseInline(instance=user)


    return render(request, 'profile.html', {'user': user,
                                            'userforms': userforms,
                                            'probases': probases,
                                            'age': age,
    })
