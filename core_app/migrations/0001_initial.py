# Generated by Django 5.0 on 2023-12-22 17:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notebooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('manufacturer', models.CharField(max_length=200)),
                ('diagonal', models.CharField(max_length=30)),
                ('screen_resolution', models.CharField(max_length=30)),
                ('os', models.CharField(max_length=50)),
                ('processor', models.CharField(max_length=100)),
                ('op_mem', models.CharField(max_length=50)),
                ('type_video_card', models.CharField(max_length=50)),
                ('video_card', models.CharField(max_length=100)),
                ('type_drive', models.CharField(max_length=50)),
                ('capacity_drive', models.CharField(max_length=100)),
                ('auto_work_time', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Ноутбуки',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(max_length=255, unique=True)),
                ('notebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='core_app.notebooks')),
            ],
            options={
                'verbose_name': 'Изображение',
            },
        ),
    ]
