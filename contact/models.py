from django.db import models
from django.core import validators

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(validators=[validators.EmailValidator(
        message="Please, enter corresponding email address")], max_length=128)
    comment = models.TextField(max_length=250)
    user_info = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name
