# Generated by Django 4.1 on 2022-11-06 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0007_alter_post_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='calorie_count',
        ),
        migrations.AddField(
            model_name='post',
            name='food_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 6, 9, 55, 54, 643351, tzinfo=datetime.timezone.utc)),
        ),
    ]
