# Generated by Django 5.1.7 on 2025-04-01 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_perfilusuario_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfilusuario',
            name='puede_comentar',
        ),
        migrations.RemoveField(
            model_name='perfilusuario',
            name='puede_publicar',
        ),
        migrations.RemoveField(
            model_name='perfilusuario',
            name='usuario',
        ),
        migrations.AlterField(
            model_name='perfilusuario',
            name='biografia',
            field=models.TextField(blank=True, null=True),
        ),
    ]
