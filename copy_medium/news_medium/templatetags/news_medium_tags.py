from django import template

from news_medium.models import CategoryArticle

register = template.Library()

@register.simple_tag()
def get_5_tags():
    return CategoryArticle.objects.all()[:5]

@register.simple_tag()
def get_tags():
    return CategoryArticle.objects.all()

