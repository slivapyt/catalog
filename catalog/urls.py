from django.urls import path
from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.Main.as_view(), name='main'),
    path('base/', views.Base.as_view(), name='base'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('about_company/', views.About_company.as_view(), name='about_company'),
    path('delivery/', views.Delivery.as_view(), name='delivery'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('stock/', views.Stock.as_view(), name='stock'),
    path('support/', views.Support.as_view(), name='support'),
    path('vacancies/', views.Vacancies.as_view(), name='vacancies'),
    path('create_product/', views.ProductCreateView.as_view(), name='create_product'),
    path('edit/<int:pk>', views.ProductUpdateView.as_view(), name='update_product'),
    path('category_edit/<int:pk>',views.CategoryUpdateView.as_view(), name='category_edit'),
    path('delete/<int:pk>', views.ProductDeleteView.as_view(), name='delete_product'),
    path('catalog/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='view'),
    path('activity/<int:pk>/', views.toggle_activity, name='toggle_activity')
]
