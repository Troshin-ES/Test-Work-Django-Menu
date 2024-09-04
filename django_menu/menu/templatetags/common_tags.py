from django import template
from menu.models import Menu, MenuItems

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, name_menu, **kwargs):
    if kwargs:
        nodes = kwargs['nodes']
        prevision_node = kwargs['prevision_node']
    else:
        all_nodes_menu = MenuItems.objects.filter(name_menu__name=name_menu)
        nodes = [top_node for top_node in all_nodes_menu if
                 top_node.parent is None]
        prevision_node = None

    if 'request' in context:
        if context['request'].path
        # print(dir(context['request']))
        print(context['request'].path)
    #     print(context['request'])
    return {'name_menu': name_menu,
            'nodes': nodes,
            'prevision_node': prevision_node}


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu_v2(context, name_menu, **kwargs):
    if 'request' in context:
        print(context['request'])

