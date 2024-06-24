from django.urls import path
from blog.apps import BlogConfig
from blog.views import MaterialCreateView, MaterialListView, MaterialDetailView, MaterialUpdateView, MaterialDeleteView
app_name =  BlogConfig.name


urlpatterns = [
    path('create/', MaterialCreateView.as_view(), name='create_material'),
    path('', MaterialListView.as_view() , name='list'),
    path('view/<int:pk>/', MaterialDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', MaterialUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', MaterialDeleteView.as_view(), name='delete'),
]

