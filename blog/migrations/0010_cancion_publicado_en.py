# Generated by Django 5.1.7 on 2025-04-01 20:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_cancion'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancion',
            name='publicado_en',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
