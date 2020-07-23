from django.contrib import admin

from .models import Book, Publisher, Author

#@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    list_display_links = ['title']
    fields = ['title', 'authors', 'publisher', 'pub_date']
    search_fields = ['title', 'authors', 'publisher', 'pub_date']

admin.site.register(Book, BookAdmin)
admin.site.register(Publisher)
admin.site.register(Author)

