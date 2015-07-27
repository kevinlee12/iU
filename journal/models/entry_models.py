# coding: utf-8
#
# Copyright 2015 The iU Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


from .utilities import shorten

from django.core.files.storage import FileSystemStorage
# The following are used for activity and entry logging.

fs = FileSystemStorage(location=settings.MEDIA_ROOT)


class Entry(models.Model):
    """Entry object used for journaling"""
    ENTRY_TYPES = (
        ('text', 'Text'),
        ('image', 'Image'),
        # ('v', 'Video'),
        ('link', 'Link'),
    )
    stu_pk = models.IntegerField()
    activity_pk = models.CharField(max_length=30)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    entry_type = models.CharField(max_length=6, choices=ENTRY_TYPES)
    text_entry = models.TextField(blank=True)
    image_entry = ProcessedImageField(processors=[Thumbnail(800, 600)],
                                      format='JPEG',
                                      options={'quality': 80},
                                      blank=True, storage=fs)
    link_entry = models.URLField(blank=True)

    def __str__(self):
        if self.text_entry:
            return shorten(self.text_entry, 50)
        return str(self.image_entry) or str(self.link_entry)

    def is_valid_entry(self):
        count = bool(self.text_entry) + bool(self.image_entry) + \
                bool(self.link_entry)
        return count < 2

    def correct_entry_type(self):
        if self.text_entry:
            self.entry_type = 'text'
        elif self.image_entry.name:
            self.entry_type = 'image'
        elif self.link_entry:
            self.entry_type = 'link'

    def save(self, *args, **kwargs):
        self.correct_entry_type()
        if not self.is_valid_entry():
            return  # Don't save it not valid
        super(Entry, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/entry/{0}/{1}/#{2}'.format(self.activity_pk, self.pk, self.entry_type)
