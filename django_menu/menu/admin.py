from django.contrib import admin
from menu.models import Menu, MenuItems


class MenuInLine(admin.TabularInline):
    model = MenuItems


class MenuItemsAdmin(admin.ModelAdmin):
    inlines = [MenuInLine]


admin.site.register(Menu, MenuItemsAdmin)
