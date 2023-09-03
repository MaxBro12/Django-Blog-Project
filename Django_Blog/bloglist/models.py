from django.db import models


# Create your models here.
class Blogs(models.Model):
    name = models.CharField('Название', max_length=100)
    article = models.CharField('', max_length=250)
    text = models.TextField('Текст')
    date = models.DateField('Дата')
