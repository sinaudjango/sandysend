# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-22 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0010_auto_20191022_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='storyline',
            field=models.TextField(),
        ),
    ]
