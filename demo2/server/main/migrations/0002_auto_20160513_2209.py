# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-13 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortener',
            name='short_url',
            field=models.CharField(max_length=200),
        ),
    ]
