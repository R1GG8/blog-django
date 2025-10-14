from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts():
    posts = Post.published.all()[:3]
    return {'posts': posts}