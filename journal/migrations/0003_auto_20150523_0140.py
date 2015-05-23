# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_auto_20150523_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='school_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(),
        ),
    ]
