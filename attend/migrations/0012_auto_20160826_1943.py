# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-26 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attend', '0011_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='createdAt',
        ),
        migrations.AddField(
            model_name='class',
            name='lastmarkedAt',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
