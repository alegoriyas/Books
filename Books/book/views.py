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

def search_form(request):
    return render(request, 'book/search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Введите поисковый запрос.')
        elif len(q) > 20:
            errors.append('Введите не более 20 символов.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'book/search.html', {'books': books, 
                                                    'query':q})
    return render(request, 'book/search_form.html', {'errors': errors})