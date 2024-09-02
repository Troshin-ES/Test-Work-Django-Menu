from django import template
from menu.models import Menu
register = template.Library()


# show_menu(None)
@register.inclusion_tag('menu.html')
def draw_menu(name_menu, *args
              # nodes, prevision_node
              ):
    print(args)
    if nodes is None:
        nodes = Menu.objects.filter(name_menu=name_menu)
        top_nodes = [node for node in nodes if node.parent is None]
        return {'nodes': top_nodes}
    return {'name_menu': name_menu,
            # 'request': request,
            # 'current_url': current_url,
            'nodes': nodes,
            'prevision_node': prevision_node}


