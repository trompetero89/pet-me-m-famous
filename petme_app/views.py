from django.contrib.auth import login, logout
from djanco.urls import reverse_lazy
from django.view.generic import CreateView
from . import forms


# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "petme/signup.html"

