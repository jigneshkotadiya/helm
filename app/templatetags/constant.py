from django.conf import settings
from django import template

register = template.Library()

@register.simple_tag
def constant_debug():
    return settings.DEBUG
