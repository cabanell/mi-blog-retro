# Generated by Django 5.1.7 on 2025-04-01 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_mensajecontacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilusuario',
            name='nombre',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
