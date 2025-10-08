from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title':'Home - Главная страница',
        'content':'Магазин мебели HOME',
    }
    return render(request, "main/index.html", context)
    # return HttpResponse("Asdsdsd")


def about(request):
    
    context = {
        'title':'Home - О нас',
        'content':'O нас',
        'text_on_page': 'Текст o магазине и товаре.',
    }
    return render(request, "main/about.html", context)
    #return HttpResponse("About")


