"""
Definition of urls for contact.
"""

from django.conf.urls import url
from . import views

app_name = 'book'

urlpatterns = [
    # /contact/
    url(r'^$', views.contact, name='contact'),
]
