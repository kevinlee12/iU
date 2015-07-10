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

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^welcome/', views.welcome, name='welcome'),
    url(r'^activities/$', views.activities, name='cabinet'),
    url(r'^activity_form/$', views.activity_form, name='activity_form'),
    url(r'^activity_form/(?P<activity_pk>[0-9]+)', views.activity_form, name='activity_form'),
    url(r'^activity/(?P<activity_id>[0-9]+)', views.entries, name='entries'),
    url(r'^entry_form/(?P<activity_id>[0-9]+)/$', views.entry_form, name='entry_form'),
    url(r'^entry_form/(?P<activity_id>[0-9]+)/(?P<entry_type>[til])/$', views.entry_form, name='entry_form'),
    url(r'^entry_form/(?P<activity_id>[0-9]+)/(?P<entry_type>[til])/(?P<entry_pk>[0-9]+)', views.entry_form, name='entry_form'),
    url(r'^delete_entry/(?P<activity_id>[0-9]+)/(?P<entry_pk>[0-9]+)', views.delete_entry, name='delete_entry'),
]
