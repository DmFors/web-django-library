from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cost = models.FloatField(validators=[MinValueValidator(0)])
    publish_year = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(2022)])

    @staticmethod
    def get_absolute_url():
        return reverse('book_list')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
