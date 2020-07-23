from django.contrib import admin

from .models import Book

#@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')
    list_display_links = ['name']
    fields = ['name']
    search_fields = ['name', 'pub_date']

admin.site.register(Book, BookAdmin)

