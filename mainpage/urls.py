"""watchlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list/(?P<list_id>[0-9]+)/$', views.ListViewPage.as_view(), name="viewlist"),
    url(r"^list/new$", views.newlist, name="newlist"),
    url(r"^list/(?P<list_id>[0-9]+)/new$", views.newentry, name="newentry"),
    url(r"^list/(?P<list_id>[0-9]+)/(?P<entry_id>[0-9]+)/delete", views.deleteentry, name="deleteentry"),
    url(r"^list/(?P<list_id>[0-9]+)/delete", views.deletelist, name="deletelist"),
    url(r'^$', views.IndexPage.as_view(), name="index"),
]
