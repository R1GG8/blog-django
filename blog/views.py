from django.shortcuts import redirect, render, get_object_or_404
from .models import Post, Category
from .forms import Post, PostForm


def post_list(request):
    posts = Post.published.all()

    context = {
        'title': 'Блог',
        'posts': posts,
    }

    return render(request, 'blog/post_list.html', context=context)


def post_list_by_category(request, category_slug):
    posts = Post.published.filter(category__slug=category_slug)

    context = {
        'title': category_slug,
        'posts': posts,
    }

    return render(request, 'blog/post_list_by_category.html', context=context)


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    context = {
        'title': post.title,
        'post': post,
    }

    return render(request, 'blog/post_detail.html', context=context)


def addpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form_commit = form.save(commit=False)
            form_commit.author = request.user
            form_commit.save()
            return redirect('blog:post_list')

    else:
        form = PostForm()

    context = {
        'title': 'Добавление поста',
        'form': form,
    }

    return render(request, 'blog/addpost.html', context=context)

