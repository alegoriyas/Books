from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=60)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name = 'e-mail')

    class Meta:
        verbose_name_plural = 'Авторы'
        verbose_name = 'Автор'

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def my_property(self):
        return self.first_name + ' ' + self.last_name
    my_property.short_description = "Full name of person"
    my_property.admin_order_field = 'last_name'

    full_name = property(my_property)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pub_date = models.DateField()       # models.DateField();  models.DateTimeField(auto_now_add=True, dЬ_index=True)

    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'Книга'
        ordering = ['-pub_date']

    def __str__(self):
        return self.title