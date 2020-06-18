"""
Definition of urls for book.
"""

from django.conf.urls import url
from . import views

app_name = 'book'

urlpatterns = [
    # /book/
    url(r'^$', views.index, name='index'),
]
