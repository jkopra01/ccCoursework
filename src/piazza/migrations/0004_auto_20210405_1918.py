# Generated by Django 3.0.2 on 2021-04-05 19:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('piazza', '0003_auto_20210405_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='post',
            name='extimestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 19, 18, 5, 901608, tzinfo=utc)),
        ),
    ]
