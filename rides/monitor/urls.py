from django.conf.urls import include, url

import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^history/$', views.history, name='history'),
    url(r'^pay_method/$', views.pay_method, name='pay_method'),
    url(r'^coords/$', views.coords, name='coords'),
]
