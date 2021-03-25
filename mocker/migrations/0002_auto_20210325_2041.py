# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2021-03-25 15:11
from __future__ import unicode_literals

from django.db import migrations


def populate_users(apps, schema_editor):
    user_model = apps.get_model('mocker', 'Users')
    user_model.objects.create(username='John Doe', pk=1)
    user_model.objects.create(username='Mark Zucky', pk=2)
    user_model.objects.create(username='Kendey Markus', pk=3)
    user_model.objects.create(username='Jeniffer Louis', pk=4)

class Migration(migrations.Migration):

    dependencies = [
        ('mocker', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_users)
    ]
