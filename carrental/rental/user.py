from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from . import models

def login(request):
    return render(request,'login.html.jinja')

def logout(request):
    return render(request,'logout.html.jinja')

def register(request):
    form = inlineformset_factory(models.RegistrationForm, models.AddressForm)
    return render(request,'register.html.jinja', {'form': form})