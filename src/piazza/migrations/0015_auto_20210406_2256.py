# Generated by Django 3.0.2 on 2021-04-06 22:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('piazza', '0014_auto_20210406_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='extimestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 22, 56, 21, 447845, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postaction',
            name='timeLeft',
            field=models.IntegerField(),
        ),
    ]