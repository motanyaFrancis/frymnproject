# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-28 18:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20170428_2322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='mfd_date',
        ),
    ]