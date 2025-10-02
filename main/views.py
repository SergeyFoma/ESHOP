from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title':'Home',
        'content':'Главная страница',
    }
    return render(request, "main/index.html", context)
    # return HttpResponse("Asdsdsd")


def about(request):
    return HttpResponse("About")


x = {
    1,
}
