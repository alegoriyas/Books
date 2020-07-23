from django.http import Http404

from django.shortcuts import render

import datetime

from .models import Book

def index(request):
    book_list = Book.objects.all
    now = datetime.datetime.now()
    #html = "%s." % now
    return render(request, 'book/index.html', {'book_list':book_list,
                                               'html':now})

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'book/time.html', {'current_datetime':now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404("Page does not exist")
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #now = "Через %s час(а, ов) будет %s." % (offset, dt)
    return render(request, 'book/next_time.html', {'next_time':dt,
                                                   'hour_offset':offset})