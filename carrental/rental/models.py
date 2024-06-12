from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.forms import ValidationError

class Equipment(models.Model):
    equipment = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.equipment

class Car(models.Model):
    ENGINE_TYPES = [
        ("benzynowy", "Benzynowy"),
        ("diesel", "Diesel"),
        ("hybrydowy", "Hybrydowy"),
        ("elektryczny", "Elektryczny"),
        ("wodorowy", "Wodorowy")
    ]
    GEARBOX_TYPES = [
        ("automatyczna", "Automatyczna"),
        ("manualna", "Manualna"),
        ("polautomatyczna", "Polautomatyczna"),
    ]
    CATEGORIES = [
        ("suv", "SUV"),
        ("miejski", "miejski"),
        ("terenowy", "terenowy"),
        ("van", "VAN"),
        ("sportowy", "sportowy"),
    ]
    brand = models.CharField(max_length=50, verbose_name="Marka")
    model = models.CharField(max_length=50, verbose_name="Model")
    engine_type = models.CharField(max_length=20, choices=ENGINE_TYPES, verbose_name="Typ silnika")
    seats_count = models.PositiveSmallIntegerField() 
    dors_count = models.PositiveSmallIntegerField()
    fuel_usage = models.FloatField()
    engine_power = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=20)
    equipment = models.ManyToManyField(Equipment)
    gearbox_type = models.CharField(max_length=20, choices=GEARBOX_TYPES)
    available = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORIES)

    def __str__(self) -> str:
        return f"{self.brand} {self.model} (ID: {self.id})"

class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    post_code = models.CharField(max_length=10)
    street = models.CharField(max_length=50)
    building_no = models.CharField(max_length=10)
    appartment_no = models.CharField(max_length=10)

class User(User):
    IDENTITY_DOCUMENT_TYPES = [
        ("dowod", "dowód osobisty"),
        ("paszport", "paszport"),
        ("prawo_jazdy", "prawo jazdy")
    ]
    phone = models.CharField(max_length=20)
    identity_document_type = models.CharField(max_length=20, choices=IDENTITY_DOCUMENT_TYPES)
    identity_document_no = models.CharField(max_length=20)
    # address = models.OneToOneField(Address, on_delete=models.RESTRICT)

class Order(models.Model):
    PAYMENT_METHODS = [
        ("karta", "Karta"),
        ("gotowka", "Gotowka"),
        ("przelew", "Przelew"),
        ("blik", "Blik"),
    ]
    customer = models.ForeignKey(User, on_delete=models.RESTRICT)
    car = models.ForeignKey(Car, on_delete=models.RESTRICT)
    order_value = models.DecimalField(max_digits=10, decimal_places=2)
    declared_order_duration = models.IntegerField()
    pickup_date = models.DateTimeField()
    return_date = models.DateTimeField()
    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    payment_status = models.BooleanField(default=False)

    def clean(self):
        """
        Walidacja dat odbioru i zwrotu zamówienia.
        """
        if self.pickup_date >= self.return_date:
            raise ValidationError(_('Return date must be later than pickup date.'))
        if self.pickup_date < timezone.now() or self.return_date < timezone.now():
            raise ValidationError(_('Dates must be greater than today\'s date.'))