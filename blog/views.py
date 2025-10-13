from django.shortcuts import render

def index(request):
    context = {
        'title': 'Главная',
    }

    return render(request, 'blog/index.html', context=context)