# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 06:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0007_auto_20161223_1322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machine_log',
            old_name='history_open_close',
            new_name='history_state',
        ),
        migrations.RenameField(
            model_name='machine_log',
            old_name='open_close_time',
            new_name='state_change_time',
        ),
    ]
