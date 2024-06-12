from .models import Product
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, FileInput


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name', 'description',
            'preview_img', 'category', 'price', 'date_create', 'date_change']
        widgets = {
            'product_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование продукта'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            'preview_img': FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'превью',
                'required': False
            }),
            'category': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'категория'
            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'цена'
            }),
            'date_create': DateTimeInput(attrs={
                'class': 'form-control'
            }),
            'date_change': DateTimeInput(attrs={
                'class': 'form-control'
            })
        }
