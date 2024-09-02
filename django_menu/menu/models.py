from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField('Название пункта меню', max_length=100)
    url = models.CharField('Ссылка', max_length=255)
    # position = models.PositiveIntegerField('Позиция', default=1, unique=True)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               help_text='Родительский пункт меню',
                               related_name='children')

    def __str__(self):
        return str(self.name)

    class Meta:
        # ordering = ('position',)
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

