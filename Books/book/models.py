from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField()       # models.DateField();  models.DateTimeField(auto_now_add=True, dЬ_index=True)

    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'Книга'
        ordering = ['-pub_date']

    def __str__(self):
        return self.name