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


# Thanks to:
# http://blog.jvc26.org/2011/07/31/django-remove-excess-comment-fields/

from django_comments.forms import CommentForm
from django.utils.encoding import force_text
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

import datetime


class EntryCommentForm(CommentForm):
    """
    Comment form for Entriies
    """
    def get_comment_create_data(self):
        return dict(
            content_type = ContentType.objects.get_for_model(self.target_object),
            object_pk    = force_text(self.target_object._get_pk_val()),
            comment      = self.cleaned_data["comment"],
            submit_date  = datetime.datetime.now(),
            site_id      = settings.SITE_ID,
            is_public    = True,
            is_removed   = False,
        )

EntryCommentForm.base_fields.pop('name')
EntryCommentForm.base_fields.pop('email')
EntryCommentForm.base_fields.pop('url')
