# Generated by Django 5.1.4 on 2024-12-22 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_remove_membroequipe_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membroequipe',
            name='areas',
        ),
        migrations.RemoveField(
            model_name='membroequipe',
            name='functions',
        ),
    ]