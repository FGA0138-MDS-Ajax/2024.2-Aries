# Generated by Django 5.1 on 2024-11-23 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_membroequipe_area_membroequipe_funcao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membroequipe',
            name='area',
        ),
        migrations.RemoveField(
            model_name='membroequipe',
            name='funcao',
        ),
    ]
