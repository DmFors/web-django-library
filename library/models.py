from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cost = models.FloatField()
    publish_date = models.IntegerField()

    def __str__(self):
        return self.name
