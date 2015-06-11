# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0007_auto_20150523_0313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('school_code', models.IntegerField(verbose_name=999999)),
                ('coordinator_id', models.IntegerField(verbose_name=9999)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('entry_type', models.CharField(choices=[('T', 'Text'), ('I', 'Image'), ('V', 'Video'), ('L', 'Link')], max_length=1)),
            ],
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='school_id',
            new_name='school_code',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_id',
            new_name='student_code',
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(default='default', max_length=30),
        ),
    ]
