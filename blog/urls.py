from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('addpost/', views.addpost, name='addpost'),
    path('<slug:category_slug>/', views.post_list_by_category, name='post_list_by_category'),
    path('post_detail/<slug:post_slug>/', views.post_detail, name='post_detail'),
]
