#from django.shortcuts import render
#from .models import Book

#def index(request):
    #book_list = Book.objects.order_by('-pub_date')[:10]
    #return render('index.html', {'book_list':book_list})

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")