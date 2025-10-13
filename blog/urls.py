from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.post_list, name='post_list'),
    path('post_detail/<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('addpost/', views.addpost, name='addpost'),
]
