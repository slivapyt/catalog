from django.shortcuts import render
from django.contrib.auth import logout, forms
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserProfileForm, UserRegisterForm
from users.models import User

def my_logout_view(request):
    logout(request)
    return redirect('/')


class RegisterView(CreateView):
    model = UserWarning
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    

class ProfileView(UpdateView):
    model = User 
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
