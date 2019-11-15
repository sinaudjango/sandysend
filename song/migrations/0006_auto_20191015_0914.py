# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-15 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0005_auto_20191013_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.CharField(choices=[('pop', 'Pop Genre'), ('rock', 'Rock'), ('metal', 'Metal'), ('islamic', 'Islamic'), ('rnb', 'RnB'), ('campursari', 'Campursari'), ('hiphop', 'Hip Hop'), ('jazz', 'Jazz'), ('dangdut', 'Dangdut')], max_length=100),
        ),
    ]
