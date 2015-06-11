# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0013_auto_20150611_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
