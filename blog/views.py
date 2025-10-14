from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render, get_object_or_404
from .models import Post, Category
from .forms import Post, PostForm
from django.views.decorators.http import require_POST


def post_list(request):
    posts = Post.published.all()

    paginator = Paginator(posts, 3)
    page = request.GET.get("page", 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:

        # Если page_number не целое число, то
        # выдать первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    # Если page_number находится вне диапазона, то
    # выдать последнюю страницу


    context = {
        'title': 'Блог',
        'posts': posts,
    }

    return render(request, 'blog/post_list.html', context=context)


def post_list_by_category(request, category_slug):
    posts = Post.published.filter(category__slug=category_slug)

    paginator = Paginator(posts, 3)
    page = request.GET.get("page", 1)
    posts = paginator.page(page)

    context = {
        'title': category_slug,
        'posts': posts,
    }

    return render(request, 'blog/post_list_by_category.html', context=context)


def post_detail(request, post_slug):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post_slug)

    context = {
        'title': post.title,
        'post': post,
    }

    return render(request, 'blog/post_detail.html', context=context)


def addpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
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


@require_POST
def delete_post(request, post_id):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, id=post_id)

    post.delete()

    return redirect("blog:post_list")


def edit_post(request, post_id):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(post.get_absolute_url())
    
    else:
        form = PostForm(instance=post)

    context = {
        'title': 'Редактирование поста',
        'form': form,
    }

    return render(request, 'blog/edit_post.html', context=context)


