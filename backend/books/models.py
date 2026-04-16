from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    rating = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.title
# Create your models here.
