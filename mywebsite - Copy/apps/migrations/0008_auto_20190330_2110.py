# Generated by Django 2.1.5 on 2019-03-30 15:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apps', '0007_auto_20190330_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=False, to='apps.Image')),
                ('user', models.ForeignKey(on_delete=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='preference',
            unique_together={('user', 'post', 'value')},
        ),
    ]
