# Generated by Django 3.0.2 on 2021-03-30 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piazza', '0003_auto_20210330_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='poster',
            field=models.CharField(max_length=60),
        ),
    ]
