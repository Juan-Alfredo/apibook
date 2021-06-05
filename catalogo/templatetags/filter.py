from django import template

register = template.Library()

@register.filter("split_name")
def split_name(value):
    return value.split(" ")