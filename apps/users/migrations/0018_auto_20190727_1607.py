# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-07-27 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20190727_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpro',
            name='gender',
            field=models.CharField(choices=[('female', '女'), ('male', '男')], default='男', max_length=5),
        ),
    ]
