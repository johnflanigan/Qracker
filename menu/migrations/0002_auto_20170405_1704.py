# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user_id',
        ),
        migrations.AddField(
            model_name='order',
            name='user_name',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
