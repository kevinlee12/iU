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


from actstream.models import user_stream
from django.http import HttpResponseRedirect
from django.shortcuts import render
import itertools


def unread_notifications_count(request):
    """Returns the number of unseen notifications"""
    count = len(list(itertools.filterfalse(lambda x: x.data['seen'],
                     user_stream(request.user))))
    return render(request, 'journal/unread_count.html',
                  {'unread_count': count})


def reset_notifications_count(request):
    def set_seen(action):
        action.data['seen'] = True
        action.save()
    list(map(set_seen, user_stream(request.user)))
    return HttpResponseRedirect('/activities')
