# Generated by Django 3.1.5 on 2021-01-14 09:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0002_auto_20210114_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='response_time',
            field=models.DurationField(default=datetime.timedelta(0), verbose_name='Reponse Time'),
        ),
    ]