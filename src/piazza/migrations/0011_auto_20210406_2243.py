# Generated by Django 3.0.2 on 2021-04-06 22:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('piazza', '0010_auto_20210406_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='extimestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 22, 43, 4, 234872, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postaction',
            name='timeLeft',
            field=models.IntegerField(),
        ),
    ]
