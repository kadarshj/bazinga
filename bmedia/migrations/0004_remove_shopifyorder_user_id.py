# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-08-09 11:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bmedia', '0003_auto_20190809_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopifyorder',
            name='user_id',
        ),
    ]
