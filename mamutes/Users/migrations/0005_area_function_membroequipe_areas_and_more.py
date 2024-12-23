# Generated by Django 5.1 on 2024-11-24 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_remove_membroequipe_area_remove_membroequipe_funcao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='membroequipe',
            name='areas',
            field=models.ManyToManyField(blank=True, related_name='membros', to='Users.area'),
        ),
        migrations.AddField(
            model_name='membroequipe',
            name='functions',
            field=models.ManyToManyField(blank=True, related_name='membros', to='Users.function'),
        ),
    ]
