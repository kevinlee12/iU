# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('student_email', models.EmailField(max_length=254)),
                ('school_id', models.IntegerField(max_length=6)),
                ('student_id', models.IntegerField(max_length=4)),
                ('personal_code', models.CharField(max_length=7)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
