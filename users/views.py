from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from blog.models import Post
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Добро пожаловать, {user.username}!")
            return redirect("users:profile")
        else:
            return render(request, "users/login.html", {"form": form, "error": "Неверный логин или пароль"})

    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, f"Вы вышли из аккаунта")
    return redirect("blog:post_list")


def signup_view(request):

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f"Вы зарегистрировались! Теперь можете войти в свой аккаунт")
            return redirect("blog:post_list")
        
    else:
        form = CustomUserCreationForm()

    return render(request, "users/signup.html", {"form": form})


@login_required(login_url='/users/login/')
def profile(request):
    posts_author = User.objects.get(id=request.user.id)
    posts = Post.objects.filter(author=posts_author)

    paginator = Paginator(posts, 3)
    page = request.GET.get("page", 1)
    posts = paginator.page(page)

    return render(request, "users/profile.html", {'posts': posts})
