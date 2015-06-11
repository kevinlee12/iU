# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0008_auto_20150611_2103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_code',
            new_name='student_id',
        ),
    ]
