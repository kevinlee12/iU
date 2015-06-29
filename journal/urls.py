from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^welcome/', views.welcome, name='welcome'),
    url(r'^activities/', views.activities, name='cabinet'),
    url(r'^activity_form/', views.activity_form, name='activity_form'),
]
