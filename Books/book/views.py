from django.shortcuts import render

from .models import Book

def index(request):
    book_list = Book.objects.order_by('-pub_date')#[:10]
    context = {'book_list':book_list}
    return render(request, 'book/index.html', context)
   
   #s = 'Список книг\r\n\r\n'
    #for b in Book.objects.order_by('-pub_date'):
        #s +=b.name + '\r\n' + str(b.pub_date) + '\r\n\r\n'
    
    #return HttpResponse(s, content_type='text/plain; charset=utf-8')

#from django.http import HttpResponse
#import datetime

#def index(request):
    #now = datetime.datetime.now()
   # return HttpResponse(now)