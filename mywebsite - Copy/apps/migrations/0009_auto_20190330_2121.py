# Generated by Django 2.1.5 on 2019-03-30 15:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apps', '0008_auto_20190330_2110'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='preference',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='preference',
            name='post',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='user',
        ),
        migrations.RemoveField(
            model_name='image',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='image',
            name='likes',
        ),
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Preference',
        ),
    ]
