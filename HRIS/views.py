from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login

from .forms import LoginForm

def home(request):
    if request.method == 'POST':
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username = loginform.cleaned_data['username']
            password = loginform.cleaned_data['password']

            user = authenticate(username = username, password = password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.session['username'] = username
                    return render(request, 'home.html', {'username': username})
                else:
                    return render(request, 'home.html')
            else:
                return render(request, 'home.html', {'loginform': loginform,})
    else:
        loginform = LoginForm()

    return render(request, 'home.html', {'loginform': loginform})
