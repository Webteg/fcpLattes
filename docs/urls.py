from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^inf/$', views.inf, name='inf'),
    url(r'^professor/$', views.professor, name='professor'),
    url(r'^geraDisplayDict/$', views.geraDisplayDict, name='geraDisplayDict'),
    url(r'^geraResp/$', views.geraResp, name='geraResp'),
]



