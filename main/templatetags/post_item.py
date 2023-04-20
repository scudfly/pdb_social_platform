from django import template
register = template.Library()

@register.inclusion_tag('post_item.html')
def post_item(item):
    return {'item': item}