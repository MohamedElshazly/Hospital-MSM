# Generated by Django 3.1.5 on 2021-01-21 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0008_auto_20210121_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='hospital',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='med.hospital'),
        ),
    ]
