from django import template
from menu.models import Menu
register = template.Library()


# show_menu(None)
@register.inclusion_tag('menu.html')
def show_menu(nodes, prevision_node):
    if nodes is None:
        nodes = Menu.objects.all()
        top_nodes = [node for node in nodes if node.parent is None]
        return {'nodes': top_nodes}
    return {'nodes': nodes,
            'prevision_node': prevision_node}
