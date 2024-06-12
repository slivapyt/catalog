# Generated by Django 5.0.6 on 2024-05-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='наименование продукта')),
                ('description', models.CharField(max_length=100, verbose_name='описание')),
                ('preview_img', models.ImageField(blank=True, null=True, upload_to='', verbose_name='превью')),
                ('category', models.CharField(max_length=100, verbose_name='категория')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('date_create', models.DateTimeField(verbose_name='дата создания')),
                ('date_change', models.DateTimeField(verbose_name='дата последнего изменения')),
            ],
        ),
    ]
