from django.shortcuts import render, redirect
from . import forms

def login(request):
    return render(request,'login.html.jinja')

def logout(request):
    return render(request,'logout.html.jinja')

def register(request):
    if request.method == 'POST':
        form_user = forms.RegistrationForm(request.POST)
        form_address = forms.UserAddressFormSet(request.POST)
        if form_user.is_valid() and form_address.is_valid():
            user = form_user.save()
            addresses = form_address.save(commit=False)
            for address in addresses:
                address.user = user
                address.save()
            return render(request,'register.html.jinja', {'message': "Success!"})
        return render(request,'register.html.jinja', {'message': "Coś nie poszło!"})
    else:
        form_user = forms.RegistrationForm()
        form_address = forms.UserAddressFormSet()
        return render(request,'register.html.jinja', {'form_user': form_user, 'form_address': form_address})