# Generated by Django 2.2 on 2020-02-29 08:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200223_0652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name': 'Todo item', 'verbose_name_plural': 'Todo items'},
        ),
        migrations.AlterModelOptions(
            name='todolist',
            options={'verbose_name': 'Todo list', 'verbose_name_plural': 'Todo lists'},
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
