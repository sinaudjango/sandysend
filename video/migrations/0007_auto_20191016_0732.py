# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-16 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0006_auto_20191016_0728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='author',
            new_name='director',
        ),
        migrations.AddField(
            model_name='video',
            name='storyline',
            field=models.TextField(default='resume film ini ya kakak'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='writers',
            field=models.CharField(default='Rahmad Sandy Kurnia', max_length=200),
            preserve_default=False,
        ),
    ]
