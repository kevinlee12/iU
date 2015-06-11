# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0012_auto_20150611_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 11, 22, 55, 58, 203119)),
        ),
        migrations.AddField(
            model_name='entry',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 11, 22, 55, 58, 203077)),
        ),
    ]
