# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-22 18:16
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0011_auto_20191022_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='storyline',
            field=ckeditor.fields.RichTextField(),
        ),
    ]