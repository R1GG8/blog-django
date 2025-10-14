from django import template
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