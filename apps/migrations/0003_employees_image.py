# Generated by Django 2.1.5 on 2019-03-03 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_employees'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]