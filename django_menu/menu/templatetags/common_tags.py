from django import template
from menu.models import Menu
register = template.Library()


# show_menu(None)
@register.inclusion_tag('menu.html')
def show_menu(nodes, prevision_node):
    if nodes is None:
        nodes = Menu.objects.all()
        return {'nodes': top_nodes(nodes)}
    return {'nodes': nodes,
            'prevision_node': prevision_node}


def top_nodes(nodes):
    return [node for node in nodes if node.parent is None]
