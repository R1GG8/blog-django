from django.shortcuts import render
from .models import Post, Category

def index(request):
    context = {
        'title': 'Главная',
    }

    return render(request, 'blog/index.html', context=context)


def about(request):
    context = {
        'title': 'О сайте',
    }

    return render(request, 'blog/about.html', context=context)


def post_list(request):
    posts = Post.published.all()

    context = {
        'title': 'Блог',
        'posts': posts,
    }

    return render(request, 'blog/post_list.html', context=context)