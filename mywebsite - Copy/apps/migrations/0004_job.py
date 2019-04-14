# Generated by Django 2.1.5 on 2019-03-07 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_employees_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('summary', models.CharField(max_length=200)),
            ],
        ),
    ]
