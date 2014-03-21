from django import template
from django.forms import CheckboxInput

register = template.Library()

@register.filter
def addclass(field, name):
       return field.as_widget(attrs={"class":name})

@register.filter(name='is_checkbox')
def is_checkbox(field):
     return field.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__
