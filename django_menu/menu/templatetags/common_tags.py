from django import template
from menu.models import Menu
register = template.Library()


def sub_menu(sub_menu_item, menu_items):
    for menu_item in menu_items:
        if menu_item.id == sub_menu_item.parent:
            print(sub_menu_item)


@register.inclusion_tag('menu.html')
def show_menu():
    menu_items = Menu.objects.all()
    res = []
    for menu_item in list(menu_items):
        sort_menu(menu_item, res)
    print(res)
    print('stop')
    # for menu_item in menu_items:
    #     print('')
    #     if menu_item.parent is None:
    #         print(menu_item.name)
    #         print(menu_item.parent)
    #         print(menu_item.children.all())
    #         continue
    #     if menu_item.parent is not None:
    #         print(menu_item.name)
    #         print(menu_item.parent)
    #         print(menu_item.children)
    #     # sub_menu(menu_item, menu_items)
    # return {'menu_items': menu_items}


# def sort_menu(menu_items, res):
#     for menu_item in menu_items:
#         # if menu_item.parent is None:
#         #     sort_menu[menu_item.name] = menu_item.url
#         res.append(menu_item)
#         if menu_item.children is not None:
#             children = menu_item.children.all()
#             sort_menu(list(children), res)
#
#         menu_items.remove(menu_item)

def sort_menu(menu_item, res: list):
    if menu_item is not res:
        print(res)
        print(menu_item)
        res.append(menu_item)
        if menu_item.children is not None:
            children = menu_item.children.all()
            list(map(sort_menu, children, res))
            # res = sort_menu(list(children), res)
        return res

def search_top_menu(menu_item):
    if menu_item.parent is not None:
        top_menu = search_top_menu(menu_item.parent)
    else:
        top_menu = menu_item
    return top_menu

show_menu()

# show_menu(None)
@register.inclusion_tag('menu.html')
def show_menu_h(menu_items):
    if menu_items is None:
        menu_items = Menu.objects.all()
    return {'menu_items': menu_items}


if __name__ == '__main__':
    from menu.templatetags.common_tags import show_menu
    show_menu(None)
