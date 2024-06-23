from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from users.models import User
from django.http import HttpResponseRedirect
from users.forms import UserRegistrationForm, UserLoginForm


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Не сохраняется в бд
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return HttpResponseRedirect(reverse('users:login_user'))
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
        'title': 'Register in website'
    }
    return render(request, 'users/register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('myblog:index'))
        else:
            return render(request, 'users/login.html', {'form': form})
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('myblog:index'))