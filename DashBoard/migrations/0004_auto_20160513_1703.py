# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0003_auto_20160513_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilebasic',
            name='dob',
            field=models.DateField(auto_now=True),
        ),
    ]
