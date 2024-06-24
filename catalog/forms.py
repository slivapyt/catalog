from .models import Product, Category
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, FileInput


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ('category', 'description')



class ProductForm(ModelForm):

    class Meta:
        model = Product
        
        fields = '__all__'

