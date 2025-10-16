from django import template
from django.db.models import Q, Count
from blog.models import Post
register = template.Library()

@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts():
    posts = Post.published.all()[:3]
    return {'posts': posts}


@register.inclusion_tag('blog/tag_list.html')
def show_tags(post_id):
    post = Post.objects.get(id=post_id)
    tags = post.tags.all()
    return {'tags': tags}


@register.inclusion_tag('blog/similar_posts.html')
def show_similar_posts(post_id, count=3):
    try:
        post = Post.objects.get(id=post_id)
        
        # Получаем теги текущего поста
        post_tags_ids = list(post.tags.values_list('id', flat=True))
        
        if not post_tags_ids:
            return {'similar_posts': []}
        
        # Более точный подсчет - считаем только общие теги
        similar_posts = Post.published.filter(
            tags__id__in=post_tags_ids
        ).exclude(
            id=post.id
        ).annotate(
            same_tags=Count('tags', filter=Q(tags__id__in=post_tags_ids))
        ).order_by(
            '-same_tags',
            '-published_at'
        ).distinct()[:count]
        
        return {'similar_posts': similar_posts}
    
    except Post.DoesNotExist:
        return {'similar_posts': []}