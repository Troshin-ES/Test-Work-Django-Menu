from django.db import models


class Menu(models.Model):
    name = models.CharField('Название меню', max_length=200, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItems(models.Model):
    name_menu = models.ForeignKey(Menu, related_name='menu_items', on_delete=models.CASCADE)
    name_item = models.CharField('Название пункта меню', max_length=100)
    url = models.CharField('Ссылка', max_length=255)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               help_text='Родительский пункт меню',
                               related_name='children')

    def __str__(self):
        return f'{self.name_menu}: {self.name_item}'

    class Meta:
        ordering = ('name_menu',)
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

