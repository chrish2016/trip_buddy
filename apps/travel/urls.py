from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^travels/$', views.dashboard),
    url(r'^addtrip$', views.addtrip),
    url(r'^processtrip$', views.processtrip),
    url(r'^deletetrip/(?P<trip_id>\d+)$', views.deletetrip),
    url(r'^travels/(?P<trip_id>\d+)$', views.showtrip),
    url(r'^travels/(?P<trip_id>\d+)/jointrip$', views.jointrip),
    url(r'^canceltrip/(?P<trip_id>\d+)$', views.canceltrip),
]
