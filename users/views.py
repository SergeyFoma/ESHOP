from django.shortcuts import render

def login(request):
    title = "Авторизация"
    context= {
        "title":title,   
    }
    return render(request, "users/login.html", context)

def registration(request):
    title = "Регистрация"
    context= {
        "title":title,   
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