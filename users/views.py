from django.shortcuts import render
from django.contrib.auth import logout as auth_logout, login as auth_login,authenticate
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

from users.forms import *



def get_user(username_or_email):
    try:
        return User.objects.get(email=username_or_email)
    except User.DoesNotExist:
        try:
            return User.objects.get(username=username_or_email)
        except User.DoesNotExist:
            return None


def login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')
        user = get_user(username_or_email)
        if user and authenticate(username=user.username, password=password):
            user = authenticate(username=user.username, password=password)
            auth_login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'users/login.html', {'error': True})
    else:
        return render(request, 'users/login.html')    


 
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            auth_login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'users/register.html',
    variables,
    ) 


def logout(request):
    auth_logout(request)
    return redirect('/')