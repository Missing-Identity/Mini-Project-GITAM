# Generated by Django 4.1 on 2022-11-06 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0004_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 6, 9, 10, 18, 50559, tzinfo=datetime.timezone.utc)),
        ),
    ]
