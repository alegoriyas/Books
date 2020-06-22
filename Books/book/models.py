from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField()       # models.DateField();  models.DateTimeField(auto_now_add=True, dЬ_index=True)