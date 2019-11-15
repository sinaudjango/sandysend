# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-21 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0011_auto_20191021_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio',
            field=models.FileField(upload_to='songs/'),
        ),
        migrations.AlterField(
            model_name='song',
            name='cover',
            field=models.ImageField(upload_to='images/'),
        ),
    ]