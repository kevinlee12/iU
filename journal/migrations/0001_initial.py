# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.core.files.storage
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '__first__'),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=30)),
                ('activity_description', models.TextField(max_length=150)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('activity_adviser', models.CharField(max_length=50)),
                ('advisor_email', models.EmailField(blank=True, null=True, max_length=254)),
                ('advisor_phone', models.CharField(blank=True, null=True, max_length=15, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format:                                 '+999999999'. Up to 15 digits allowed.")])),
            ],
        ),
        migrations.CreateModel(
            name='ActivityOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_email', models.EmailField(max_length=254)),
                ('activity_pk', models.CharField(max_length=30)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('entry_type', models.CharField(max_length=6, choices=[('text', 'Text'), ('image', 'Image'), ('link', 'Link')])),
                ('text_entry', models.TextField(blank=True)),
                ('image_entry', models.ImageField(blank=True, storage=django.core.files.storage.FileSystemStorage(location='/home/leekevin/iU/media'), upload_to='')),
                ('link_entry', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='LearningObjectiveOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_code', models.CharField(max_length=6)),
                ('school_name', models.CharField(max_length=30)),
                ('group', models.OneToOneField(to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('student_id', models.CharField(max_length=4)),
                ('personal_code', models.CharField(max_length=7)),
                ('stu_coordinator', models.IntegerField()),
                ('school', models.ForeignKey(to='journal.School')),
                ('user', models.OneToOneField(default=0, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=1, choices=[('S', 'Student'), ('C', 'Coordinator'), ('A', 'Advisor')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
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
            field=models.ManyToManyField(blank=True, to='journal.Student'),
        ),
        migrations.AddField(
            model_name='coordinator',
            name='user',
            field=models.OneToOneField(default=0, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='advisor',
            name='school',
            field=models.ForeignKey(to='journal.School'),
        ),
        migrations.AddField(
            model_name='advisor',
            name='students',
            field=models.ManyToManyField(blank=True, to='journal.Student'),
        ),
        migrations.AddField(
            model_name='advisor',
            name='user',
            field=models.OneToOneField(default=0, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_type',
            field=models.ManyToManyField(to='journal.ActivityOptions'),
        ),
        migrations.AddField(
            model_name='activity',
            name='entries',
            field=models.ManyToManyField(blank=True, to='journal.Entry'),
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
