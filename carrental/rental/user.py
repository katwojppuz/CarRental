from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as lgn
from . import forms

def login(request):
    if request.method == 'POST':
        form_user = forms.LoginForm(request.POST)
        print("1")
        print(form_user.errors)
        if form_user.is_valid():
            print("2")
            username = form_user.cleaned_data['username']
            password = form_user.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("3")
                lgn(request, user)
        redirect_to = request.GET.get('next', '')
        print(redirect_to)
        return HttpResponseRedirect(redirect_to) 
    else:
        form_user = forms.LoginForm()    
        return render(request,'login.html.jinja', {'form_user': form_user})

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