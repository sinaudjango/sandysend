# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-14 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_video_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(blank=True, default='images/thumbnail.jpg', upload_to='images/'),
        ),
    ]
