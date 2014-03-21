from django import template
register = template.Library()

@register.filter
def addclass(field, name):
       return field.as_widget(attrs={"class":name})
