# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 15:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('think', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='think',
            name='weixin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passport.WeixinUsers'),
        ),
    ]