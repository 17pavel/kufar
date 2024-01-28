from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.
def login(request):
    return render(request, "registration/login.html")

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
