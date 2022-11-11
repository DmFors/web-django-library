from django import template

register = template.Library()


@register.simple_tag(takes_context=True, name='return_get_params')
def return_get_params(context, **kwargs):
    params = context['request'].GET.copy()
    for param_name, param_value in kwargs.items():
        params[param_name] = param_value
    # delete waste params
    for k in [k for k, v in params.items() if not v]:
        del params[k]
    return params.urlencode()
