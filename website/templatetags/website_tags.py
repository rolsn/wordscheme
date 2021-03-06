from django.template.defaulttags import register

@register.filter(name='lookup')
def get_item(d, k):
    return d.get(k)

@register.filter(name='getlength')
def get_length(a):
    return len(a)
