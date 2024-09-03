from django import template
from menu.models import Menu, MenuItems

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, name_menu, **kwargs):
    # for i in context:
    #     if 'request' in i:
    #         print(i['request'])
    if kwargs:
        nodes = kwargs['nodes']
        prevision_node = kwargs['prevision_node']
    else:
        all_nodes_menu = MenuItems.objects.filter(name_menu__name=name_menu)
        nodes = [top_node for top_node in all_nodes_menu if
                 top_node.parent is None]
        prevision_node = None
    return {'name_menu': name_menu,
            'nodes': nodes,
            'prevision_node': prevision_node,
            'context': kwargs['context']}



