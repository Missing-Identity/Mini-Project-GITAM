# Generated by Django 4.1 on 2022-11-06 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0002_alter_post_post_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
