# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-24 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_profile_report_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='report_frequency',
            field=models.CharField(default=2, max_length=10),
        ),
    ]
