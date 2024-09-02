# Generated by Django 4.2.15 on 2024-08-31 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название пункта меню')),
                ('url', models.CharField(max_length=255, verbose_name='Ссылка')),
                ('parent', models.ForeignKey(blank=True, help_text='Родительский пункт меню', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu.menu')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
            },
        ),
    ]
