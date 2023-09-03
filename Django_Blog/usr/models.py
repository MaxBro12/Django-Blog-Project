from django.db import models


# Create your models here.
class Users(models.Model):
    login = models.CharField('username', primary_key=True, max_length=50)
    password = models.CharField('password', max_length=100)
    email = models.CharField('email', max_length=100)
