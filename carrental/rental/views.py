import pandas as pd
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Car, Order
from .forms import OrderForm

def index(request):
    return render(request,'index.html.jinja')

def cars(request):
    cars = Car.objects.all()
    categories = list(cars.values_list('category', flat=True).distinct())
    cars2 = pd.DataFrame.from_records(cars.values())
    return render(request,'cars.html.jinja', {'cars': cars, 'categories': categories, 'cars2': cars2.to_html(classes='table table-striped table-bordereds', index=False, table_id="cars2")})

def car(request, car_id):
    return render(request,'car.html.jinja')

def rent(request, car_id):
    if request.method == 'POST':
        form_order = OrderForm(request.POST)
        if form_order.is_valid():
            order = form_order.save()
            return redirect('confirm', order=order)
        return render(request,'rent.html.jinja', {'message': "Coś nie poszło!"})
    else:
        car = Car.objects.get(id=car_id)
        order = Order(
            car=car, 
            deposit=0.1*float(car.value),
        )
        form_order = OrderForm(instance=order)
    return render(request,'rent.html.jinja', {'form_order': form_order, 'car_id': car_id})

def confirm(request, order):
    return render(request,'confirm.html.jinja', {'order': order})