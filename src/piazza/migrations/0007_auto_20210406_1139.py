# Generated by Django 3.0.2 on 2021-04-06 11:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('piazza', '0006_auto_20210406_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='extimestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 11, 39, 54, 709798, tzinfo=utc)),
        ),
    ]
