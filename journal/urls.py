from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^welcome/', views.welcome, name='welcome'),
    url(r'^activities/$', views.activities, name='cabinet'),
    url(r'^activity_form/$', views.activity_form, name='activity_form'),
    url(r'^activity/(?P<activity_id>[0-9]+)/$', views.entries, name='entries'),
    url(r'^entry_form/(?P<activity_id>[0-9]+)/$', views.entry_form, name='entry_form'),
    url(r'^entry_form/(?P<activity_id>[0-9]+)/(?P<entry_pk>[0-9]+)', views.entry_form, name='entry_form'),
]
