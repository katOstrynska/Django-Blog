# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default='ddddddd'),
        ),
    ]