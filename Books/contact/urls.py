"""
Definition of urls for contact.
"""

from django.conf.urls import url
from . import views

app_name = 'contact'

urlpatterns = [
    # /contact/
    url(r'^$', views.index, name='index'),
    #url(r'^$', views.contact, name='contact'),
    url(r'^contact_form/$', views.contact_form, name='contact_form'),
]
