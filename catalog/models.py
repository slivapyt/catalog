from django.db import models
import uuid
# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(
        max_length=100, verbose_name='наименование продукта')
    description = models.CharField(max_length=100, verbose_name='описание')
    preview_img = models.ImageField(verbose_name='превью', **NULLABLE)

    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='категория'
    )
    price = models.IntegerField(verbose_name='цена')
    date_create = models.DateTimeField(verbose_name='дата создания')
    date_change = models.DateTimeField(
        verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.product_name} - {self.price} \n {self.category}'


class Category(models.Model):
    category = models.CharField(
        max_length=100, verbose_name='наименование категории')

    description = models.CharField(
        max_length=100, verbose_name='описание категории')

    def __str__(self):
        return f'{self.category}\n {self.description}'
