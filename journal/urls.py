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

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login_redirects/', views.login_redirects, name='login_redirects'),
    url(r'^accounts/login/', views.login_redirects, name='login_redirects'),
    url(r'^activities/$', views.activities, name='activities'),
    url(r'^activities/(?P<student_pk>[0-9]+)', views.activities, name='activities'),
    url(r'^activity_details/$', views.activity_details, name='activity_details'),
    url(r'^activity_details/(?P<activity_pk>[0-9]+)', views.activity_details,
        name='activity_details'),
    url(r'^advisor/$', views.advisors_form, name='advisor_form'),
    url(r'^advisor/(?P<advisor_pk>[0-9]+)', views.advisors_form, name='advisor_form'),
    url(r'^coordinator/', views.coordinator, name='coordinator'),
    url(r'^delete_activity/(?P<activity_pk>[0-9]+)', views.activity_deletion,
        name='delete_activity'),
    url(r'^entries/(?P<activity_pk>[0-9]+)', views.entries, name='entries'),
    url(r'^entry/(?P<activity_pk>[0-9]+)/$', views.entry, name='entry'),
    url(r'^entry/(?P<activity_pk>[0-9]+)/(?P<entry_pk>[0-9]+)', views.entry, name='entry'),
    url(r'^delete_entry/(?P<activity_pk>[0-9]+)/(?P<entry_pk>[0-9]+)',
        views.delete_entry, name='delete_entry'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^student/$', views.student_registration, name='student'),
    url(r'^student/(?P<student_pk>[0-9]+)/', views.student_registration, name='student'),
    url(r'^remove_student/(?P<student_pk>[0-9]+)/', views.remove_student,
        name='remove_student'),
    url(r'^comment_submit', views.comment_submit, name='submit'),
    # Old urls:
    # url(r'^delete_activity/(?P<activity_pk>[0-9]+)', views.activity_deletion,
    #     name='delete_activity'),
    # url(r'^activity_form/$', views.activity_form, name='activity_form'),
    # url(r'^activity_form/(?P<activity_pk>[0-9]+)', views.activity_form,
    #     name='activity_form'),
    # url(r'^activity/(?P<activity_id>[0-9]+)', views.entries, name='entries'),
    # url(r'^entry_form/(?P<activity_id>[0-9]+)/(?P<entry_type>[aegiklmntx]+)/$',
    #     views.entry_form, name='entry_form'),
    # url(r'^entry_form/(?P<activity_id>[0-9]+)/(?P<entry_type>[#aegiklmntx]+)/'
    #     '(?P<entry_pk>[0-9]+)/', views.entry_form, name='entry_form'),
    # url(r'^delete_entry/(?P<activity_id>[0-9]+)/(?P<entry_pk>[0-9]+)',
    #     views.delete_entry, name='delete_entry'),
    # url(r'^coordinator/', views.coordinator, name='coordinator'),
    # url(r'^student_registration/$', views.student_registration,
    #     name='student_registration'),
    # url(r'^student_registration/(?P<student_pk>[0-9]+)/',
    #     views.student_registration, name='student_registration'),
    # url(r'^student_activities/(?P<student_pk>[0-9]+)/',
    #     views.student_activities, name='student_activities'),
    # url(r'^student_entries/(?P<student_pk>[0-9]+)/(?P<activity_pk>[0-9]+)',
    #     views.student_entries, name='student_entries'),
    # url(r'^advisor_form/$', views.advisors_form, name='advisors_form'),
    # url(r'^advisor_form/(?P<advisors_pk>[0-9]+)/', views.advisors_form,
    #     name='advisors_form'),
    # url(r'^remove_student/(?P<student_pk>[0-9]+)/', views.remove_student,
    #     name='remove_student'),
    # url(r'^entry_view/(?P<student_pk>[0-9]+)/(?P<activity_pk>[0-9]+)/(?P<entry_pk>[0-9]+)/',
    #     views.view_stu_entry, name='view_stu_entry'),
]
