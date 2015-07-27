# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image_entry',
            field=imagekit.models.fields.ProcessedImageField(upload_to='', storage=django.core.files.storage.FileSystemStorage(location='/home/leekevin/iU/media'), blank=True),
        ),
    ]
