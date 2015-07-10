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
# Unless required by applicable law or agreed to in writing, softwar
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.db import models
from django.conf import settings

from django.core.files.storage import FileSystemStorage
# The following are used for activity and entry logging.

fs = FileSystemStorage(location=settings.MEDIA_ROOT)

def file_name(instance, filename):
    return instance.pk

class Entry(models.Model):
    """Entry object used for journaling"""
    ENTRY_TYPES = (
        ('t', 'Text'),
        ('i', 'Image'),
        # ('v', 'Video'),
        ('l', 'Link'),
    )
    stu_email = models.EmailField()
    activity_pk = models.CharField(max_length=30)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    entry_type = models.CharField(max_length=1, choices=ENTRY_TYPES)
    text_entry = models.TextField(blank=True)
    image_entry = models.ImageField(blank=True, upload_to=file_name)
    link_entry = models.URLField(blank=True)

    def __str__(self):
        return str(self.created) + " : " + (self.text_entry or str(self.image_entry) or str(self.link_entry))
