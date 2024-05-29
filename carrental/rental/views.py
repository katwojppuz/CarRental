import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from .models import Car

def index(request):
    return render(request,'index.html.jinja')

def cars(request):
    cars = Car.objects.all()
    categories = list(cars.values_list('category', flat=True).distinct())
    cars2 = pd.DataFrame.from_records(cars.values())
    return render(request,'cars.html.jinja', {'cars': cars, 'categories': categories, 'cars2': cars2.to_html(classes='table table-striped table-bordereds', index=False, table_id="cars2")})

def car(request, car_id):
    return render(request,'car.html.jinja')