from django.db import models

# Create your models here.
class BookModel(models.Model):
    title=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    price=models.IntegerField()

    def __str__(self):
        return self.subtitle