"""
Definition of urls for Books.
"""

from django.conf.urls import include, url


from django.contrib import admin
admin.autodiscover()

from django.views.generic import RedirectView

urlpatterns = [

    url(r'^book/', include('book.urls')),
    url(r'^$', RedirectView.as_view(url='/book/', permanent=True)),

    url(r'^admin/', include(admin.site.urls)),

]
