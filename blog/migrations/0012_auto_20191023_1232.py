# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-23 12:32
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20191023_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
