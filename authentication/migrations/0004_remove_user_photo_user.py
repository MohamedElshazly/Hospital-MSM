# Generated by Django 3.1.5 on 2021-04-07 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_user_photo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='photo_user',
        ),
    ]
