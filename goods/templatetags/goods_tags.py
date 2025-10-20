from django import template
from goods.models import Categories
from django.utils.http import urlencode

register = template.Library()

@register.simple_tag
def tag_categories():
    return Categories.objects.all()

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    #print(query)
    # example with other context vars
    #print(context['title'])
    #print(context['slug_url'])
    #print(context['goods'])
    #print([product.name for product in context['goods']])
    #print(kwargs)
    query.update(kwargs)
    print(query)
    return urlencode(query)