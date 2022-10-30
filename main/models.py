from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

from django.contrib.auth.hashers import check_password


def validate_role(value):
    if value not in (0, 1, 2):
        raise ValidationError("Роль пользователя указана неверно!")


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    role = models.PositiveSmallIntegerField(default=1, validators=[validate_role])

    def check_password(self, password):
        return check_password(password, self.password)

    @staticmethod
    def get_absolute_url():
        return reverse('book_list')
