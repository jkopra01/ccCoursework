# Generated by Django 3.0.2 on 2021-04-05 18:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('piazza', '0002_auto_20210405_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commenter',
            field=models.CharField(default='admin', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='extimestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 18, 26, 17, 778106, tzinfo=utc)),
        ),
    ]
