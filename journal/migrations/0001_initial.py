# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('activity_name', models.CharField(max_length=30)),
                ('activity_description', models.TextField(max_length=150)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('activity_adviser', models.CharField(max_length=50)),
                ('advisor_email', models.EmailField(max_length=254, blank=True, null=True)),
                ('advisor_phone', models.CharField(validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format:                                 '+999999999'. Up to 15 digits allowed.")], max_length=15, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityOptions',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('advisors', models.ManyToManyField(to='journal.Advisor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('stu_email', models.EmailField(max_length=254)),
                ('activity_pk', models.CharField(max_length=30)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('entry_type', models.CharField(max_length=6, choices=[('text', 'Text'), ('image', 'Image'), ('link', 'Link')])),
                ('text_entry', models.TextField(blank=True)),
                ('image_entry', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/home/leekevin/iU/media'), upload_to='', blank=True)),
                ('link_entry', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='LearningObjectiveOptions',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('objective', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('school_code', models.CharField(max_length=6)),
                ('school_name', models.CharField(max_length=30)),
                ('group', models.OneToOneField(to='auth.Group', default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('student_id', models.CharField(max_length=4)),
                ('personal_code', models.CharField(max_length=7)),
                ('stu_coordinator', models.IntegerField()),
                ('school', models.ForeignKey(to='journal.School')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('user_type', models.CharField(max_length=1, choices=[('S', 'Student'), ('C', 'Coordinator'), ('A', 'Advisor')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, default=0)),
            ],
        ),
        migrations.AddField(
            model_name='coordinator',
            name='school',
            field=models.ForeignKey(to='journal.School'),
        ),
        migrations.AddField(
            model_name='coordinator',
            name='students',
            field=models.ManyToManyField(to='journal.Student', blank=True),
        ),
        migrations.AddField(
            model_name='coordinator',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=0),
        ),
        migrations.AddField(
            model_name='advisor',
            name='school',
            field=models.ForeignKey(to='journal.School'),
        ),
        migrations.AddField(
            model_name='advisor',
            name='students',
            field=models.ManyToManyField(to='journal.Student', blank=True),
        ),
        migrations.AddField(
            model_name='advisor',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=0),
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_type',
            field=models.ManyToManyField(to='journal.ActivityOptions'),
        ),
        migrations.AddField(
            model_name='activity',
            name='entries',
            field=models.ManyToManyField(to='journal.Entry', blank=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='learned_objective',
            field=models.ManyToManyField(to='journal.LearningObjectiveOptions'),
        ),
        migrations.AddField(
            model_name='activity',
            name='student',
            field=models.ForeignKey(to='journal.Student'),
        ),
    ]
