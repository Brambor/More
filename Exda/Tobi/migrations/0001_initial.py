# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-13 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mydb',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('n_of_requests', models.IntegerField(default=0)),
            ],
        ),
    ]
