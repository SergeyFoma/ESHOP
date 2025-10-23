from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm

def login(request) -> HttpResponseRedirect | HttpResponse:
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserLoginForm()

    title = "Авторизация"
    context= {
        "title":title,   
        'form':form,
    }
    return render(request, "users/login.html", context)

def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users:login"))
    else:
        form = UserRegistrationForm()
    title = "Регистрация"
    context= {
        "title":title,
        "form":form,   
    }
    return render(request, "users/registration.html", context)

def profile(request):
    title = "Профиль"
    context= {
        "title":title,   
    }
    return render(request, "users/profile.html", context)

def logout(request):
    title = "Выход"
    context= {
        "title":title,   
    }
    return render(request, "users/logout.html", context)