# Generated by Django 3.0.2 on 2021-04-06 22:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('piazza', '0008_auto_20210406_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='extimestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 22, 35, 39, 626237, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postaction',
            name='timeLeft',
            field=models.IntegerField(),
        ),
    ]
