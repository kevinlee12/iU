# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0010_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='entry',
            field=models.URLField(default='www.website.com'),
        ),
    ]
