from django.contrib import admin

from .models import Book, Publisher, Author

#@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'pub_date')
    list_display_links = ['title']
    fields = ['title', 'authors', 'publisher', 'pub_date']      #Этот атрибут содержит список полей, которые будут включены в форму редактирования.
    search_fields = ['pub_date', 'authors__last_name', 'publisher__name', 'title']      #ForeignKey__nameModel and ManyToManyField__nameModel
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'             #страница списка объектов будет содержать навигацию по датам из этого поля
    ordering = ['-pub_date']
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)

admin.site.register(Book, BookAdmin)



admin.site.register(Publisher)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'full_name', 'email')
    search_fields = ['first_name', 'last_name']
    list_display_links = ['last_name']

admin.site.register(Author, AuthorAdmin)

