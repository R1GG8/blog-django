from django.shortcuts import render
from blog.models import Post

def index(request):
    posts = Post.published.all()[:3]

    context = {
        'title': 'Главная',
        'posts': posts,
    }

    return render(request, 'main/index.html', context=context)


def about(request):
    context = {
        'title': 'О сайте',
    }

    return render(request, 'main/about.html', context=context)
