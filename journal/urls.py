from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^welcome/', views.welcome, name='welcome'),
    url(r'^cabinet/', views.cabinet, name='cabinet'),
    url(r'^activity_form/', views.activity_form),
]
