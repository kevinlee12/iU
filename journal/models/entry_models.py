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

import journal.models.activity_models
from cloudinary.models import CloudinaryField

from django.core.files.storage import FileSystemStorage
# The following are used for activity and entry logging.

fs = FileSystemStorage(location=settings.MEDIA_ROOT)


class Entry(models.Model):
    """Entry object used for journaling"""
    ENTRY_TYPES = (
        ('text', 'Text'),
        ('image', 'Image'),
        ('link', 'Link'),
    )
    stu_pk = models.IntegerField()
    activity_pk = models.IntegerField()
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    entry = models.CharField(max_length=1000)
    # image_entry = ProcessedImageField(processors=[ResizeToRatio()],
    #                                   format='JPEG',
    #                                   options={'quality': 80},
    #                                   blank=True, storage=fs)

    def __str__(self):
        return journal.models.activity_models\
            .Activity.objects.get(pk=int(self.activity_pk)).activity_name


    def get_absolute_url(self):
        return '/entry/{0}/{1}/'.format(self.activity_pk, self.pk)
