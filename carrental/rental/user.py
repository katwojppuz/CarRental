from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms

def login(request):
    return render(request,'login.html.jinja')

def logout(request):
    return render(request,'logout.html.jinja')

def register(request):
    if request.method == 'GET':
        form = forms.RegistrationForm()
        form_address = forms.UserAddressFormSet
        return render(request,'register.html.jinja', {'form': form, 'form_address': form_address})
    elif request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        messages.success(request, "Success")
        return render(request,'register.html.jinja')
    else:
        return render(request,'register.html.jinja')