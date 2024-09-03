from django import template
from menu.models import Menu, MenuItems

register = template.Library()


# # show_menu(None)
# @register.inclusion_tag('menu.html')
# def draw_menu(name_menu,
#               nodes, prevision_node
#               ):
#     if nodes is None:
#         nodes = Menu.objects.filter(name_menu=name_menu)
#         top_nodes = [node for node in nodes if node.parent is None]
#         return {'nodes': top_nodes}
#     return {'name_menu': name_menu,
#             # 'request': request,
#             # 'current_url': current_url,
#             'nodes': nodes,
#             'prevision_node': prevision_node}


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, name_menu, **kwargs):
    print(type(context))
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
            'prevision_node': prevision_node}



