from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('addpost/', views.addpost, name='addpost'),
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('category/<slug:category_slug>/', views.post_list_by_category, name='post_list_by_category'),
    path('tag/<slug:tag_slug>/', views.post_list_by_tag, name='post_list_by_tag'),
    path('post_detail/<slug:post_slug>/', views.post_detail, name='post_detail'),
]
