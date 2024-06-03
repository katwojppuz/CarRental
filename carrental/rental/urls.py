from django.urls import path
from . import views
from . import user

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.cars, name='cars'),
    path('car/<car_id>', views.car, name='car'),
    path('car/rent/<car_id>', views.rent, name='rent'),
    path('car/confirm/<car_id>', views.confirm, name='confirm'),
    path('user/login', user.login, name='login'),
    path('user/logout', user.logout, name='logout'),
    path('user/register', user.register, name='register')
]