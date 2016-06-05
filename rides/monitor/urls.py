from django.conf.urls import include, url

from .views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^history/$', history, name='history'),
    url(r'^coords/$', coords, name='coords'),
]
