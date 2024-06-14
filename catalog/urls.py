from django.urls import path
from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.Main.as_view(), name='main'),
    path('base/', views.base, name='base'),
    path('contact/', views.contact, name='contact'),
    path('about_company/', views.about_company, name='about_company'),
    path('delivery/', views.delivery, name='delivery'),
    path('profile/', views.profile, name='profile'),
    path('stock/', views.stock, name='stock'),
    path('support/', views.support, name='support'),
    path('transportation/', views.transportation, name='transportation'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('create_product/', views.create_product, name='create_product'),
    path('product/', views.product, name='product'),
    path('<int:pk>', views.CategoryDetailView.as_view(), name='category-detail')
]
