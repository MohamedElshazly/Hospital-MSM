# Generated by Django 3.1.5 on 2021-01-25 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0016_auto_20210125_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.CharField(max_length=225, verbose_name='Equipment Name'),
        ),
    ]
