from django.shortcuts import render

def index(request):
    context = {
        'title': 'Главная',
    }

    return render(request, 'main/index.html', context=context)


def about(request):
    context = {
        'title': 'О сайте',
    }

    return render(request, 'main/about.html', context=context)
