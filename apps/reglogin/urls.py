"""trip_buddy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    # url(r'^dashboard$', views.dashboard),
    # url(r'^user/(?P<user_id>\d+)$', views.show),
    # url(r'^book/form$', views.bookform),
    # url(r'^book/add$', views.add),
    # url(r'^book/(?P<book_id>\d+)/$', views.bookpage),
    # url(r'^book/(?P<book_id>\d+)/minireview$', views.minireview),
    # url(r'^book/(?P<book_id>\d+)/delete', views.delete)
]
