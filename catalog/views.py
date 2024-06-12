from django.shortcuts import render, redirect
from catalog.models import Category, Product
from .forms import ProductForm
from django.views.generic import DetailView
# Create your views here.


# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'catalog/details_view.html'  # шаблон который будет обрабатывать
#     context_object_name = 'product'  # Ключ по которому передаем объект внутрь шаблона


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'catalog/category_view.html'  # шаблон который будет обрабатывать
    # Ключ по которому передаем объект внутрь шаблона
    context_object_name = 'categorys'


def main(request):
    category_list = Category.objects.all()
    if request.method == 'POST':
        change_category = request.POST.get()
    context = {
        'object_list': category_list
    }

    return render(request, 'catalog/main.html', context)


def base(request):
    return render(request, 'catalog/base.html')


def contact(request):
    return render(request, 'catalog/contact.html')


def about_company(request):
    return render(request, 'catalog/about_company.html')


def delivery(request):
    return render(request, 'catalog/delivery.html')


def profile(request):
    return render(request, 'catalog/profile.html')


def stock(request):
    return render(request, 'catalog/stock.html')


def support(request):
    return render(request, 'catalog/support.html')


def transportation(request):
    return render(request, 'catalog/transportation.html')


def vacancies(request):
    return render(request, 'catalog/vacancies.html')


def create_product(request):
    error = ''
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Форма была неверной'
    form = ProductForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'catalog/create_product.html', data)


def product(request):
    return render(request, 'catalog/product.html')
