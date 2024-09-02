from django.db import models


# Create your models here.
class Menu(models.Model):
    name_menu = models.CharField('Название меню', max_length=100)
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

