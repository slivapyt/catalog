from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from catalog.models import Category, Product
from .forms import ProductForm, CategoryForm
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'catalog/category_view.html'  # шаблон который будет обрабатывать
    context_object_name = 'categorys' # Ключ по которому передаем объект внутрь шаблона

class Main(ListView):
    model = Category
    template_name = 'catalog/main.html'
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        return queryset

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    fields = (
        'product_name', 'description', 'preview_img',
        'category', 'price', 'date_create', 'date_change')
    success_url = reverse_lazy('catalog:main')

class ProductUpdateView(UpdateView):
    model = Product
    fields = (
        'product_name', 'description', 'preview_img',
        'category', 'price', 'date_create', 'date_change')
    success_url = reverse_lazy('catalog:main')

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('main')

def toggle_activity(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    if product_item.is_active:
        product_item.is_active = False
    else:
        product_item.is_active = True
    product_item.save()
    return redirect(reverse("catalog:main"))


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:main')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset =  inlineformset_factory(Category, Product, form=ProductForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance= self.object) # instance= self.object нужно только для редактирования
        else:
            context_data['formset'] = ProductFormset(instance=self.object) # instance= self.object нужно только для редактирования
        return context_data
    
    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
            
        return super().form_valid(form)
    




















class Base(ListView):
    model = Category
    template_name = 'catalog/base.html'

class Contact(ListView):
    model = Category
    template_name = 'catalog/contact.html'

class About_company(ListView):
    model = Category
    template_name = 'catalog/about_company.html'

class Delivery(ListView):
    model = Category
    template_name = 'catalog/delivery.html'

class Profile(ListView):
    model = Category
    template_name = 'catalog/profile.html'

class Stock(ListView):
    model = Category
    template_name = 'catalog/stock.html'

class Support(ListView):
    model = Category
    template_name = 'catalog/support.html'

class Vacancies(ListView):
    model = Category
    template_name = 'catalog/vacancies.html'



