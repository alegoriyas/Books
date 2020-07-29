"""
Definition of urls for book.
"""

from django.conf.urls import url
from . import views

app_name = 'book'

urlpatterns = [
    # /book/
    url(r'^$', views.index, name='index'),
    url(r'^time/$', views.current_datetime, name='current_datetime'),
    url(r'^time/(\d{1,2})/$', views.hours_ahead, name='hours_ahead'),     #(?P<offset>\d{1,2})
    url(r'^search-form/$', views.search_form, name='search_form'),
    url(r'^search/$', views.search, name='search'),
]
