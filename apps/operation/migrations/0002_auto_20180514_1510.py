# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-14 15:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videocomments',
            old_name='title',
            new_name='comments_title',
        ),
    ]