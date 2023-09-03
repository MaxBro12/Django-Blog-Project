# Generated by Django 4.2.4 on 2023-09-03 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('article', models.CharField(max_length=250, verbose_name='')),
                ('text', models.TextField(verbose_name='Текст')),
                ('date', models.DateField(verbose_name='Дата')),
            ],
        ),
    ]