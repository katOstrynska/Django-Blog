from django import template
register = template.Library()

from ..models import Post

@register.simple_tag(name="first")
def first_function():
    return Post.objects.count()

@register.inclusion_tag('post_list.html')
def second_function(post):
    excerpts = post.excerpt.all()
    authors = post.author.all()
    return {'excerpts': excerpts, 'authors': authors}