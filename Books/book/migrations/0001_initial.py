# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-18 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]