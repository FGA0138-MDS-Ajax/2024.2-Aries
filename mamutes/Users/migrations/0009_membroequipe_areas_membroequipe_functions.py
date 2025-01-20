from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0008_remove_membroequipe_areas_and_more'),
    ]

    operations = [
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
