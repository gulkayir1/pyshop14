from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView

from account.forms import RegistrationForm
from django.urls import reverse_lazy

class RegisterView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

