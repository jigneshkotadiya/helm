from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    # work with default auth custom signup foem
    # success_url = reverse_lazy('login')
    # work with all auth
    success_url = reverse_lazy('home')
    template_name = 'users/signup.html'
