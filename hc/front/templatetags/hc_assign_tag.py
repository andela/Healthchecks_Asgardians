from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.simple_tag
def define(the_string):
    return the_string
