from django.urls import path
from users.apps import UsersConfig
from django.contrib.auth.views import LoginView

from users.views import RegisterView, my_logout_view, ProfileView


app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', my_logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),

]
