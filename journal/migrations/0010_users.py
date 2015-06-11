# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0009_auto_20150611_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('user_type', models.CharField(choices=[('S', 'Student'), ('C', 'Coordinator')], max_length=1)),
            ],
        ),
    ]
