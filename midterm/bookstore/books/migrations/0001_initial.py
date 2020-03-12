# Generated by Django 2.2 on 2020-03-02 04:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('num_pages', models.IntegerField()),
                ('genre', models.IntegerField(choices=[(1, 'HORROR'), (2, 'CLASSIC'), (3, 'DRAMA')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.IntegerField(choices=[(1, 'Bullet'), (2, 'Food'), (3, 'Travel'), (4, 'Sport')])),
                ('publisher', models.CharField(max_length=60)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
