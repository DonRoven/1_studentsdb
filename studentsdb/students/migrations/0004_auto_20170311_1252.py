# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 12:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_student_droup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_droup',
            new_name='student_group',
        ),
    ]
