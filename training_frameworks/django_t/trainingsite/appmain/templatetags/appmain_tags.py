from django import template
from appmain.models import *

register = template.Library()

@register.simple_tag(name='get_cats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag('appmain/list_categories.html')
def show_categories(cat_selected=None):
    cats = Category.objects.all()
    if not cat_selected:
        return {'cats':cats}
    else:
        return {'cats':cats, 'title':'Test'}