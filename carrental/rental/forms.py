from django.forms import ModelForm, TextInput, Select, DateInput
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import inlineformset_factory
from django.utils.translation import gettext_lazy as _
from . import models

class RegistrationForm(UserCreationForm):
    class Meta:
        model = models.User
        # exclude = ['id']
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'identity_document_type', 'identity_document_no']
        labels = {
            'phone': _("Numer telefonu"),
            'identity_document_type': _("Typ dokumentu tożsamości"),
            'identity_document_no': _("Numer dokumentu tożsamości"),
        }

class AddressForm(ModelForm):
    class Meta:
        model = models.Address
        exclude = ['id']
        labels = {
            'country': _("Kraj"),
            'city': _("Miejscowość"),
            'post_code': _("Kod pocztowy"),
            'street': _("Ulica"),
            'building_no': _("Numer budynku"),
            'appartment_no': _("Numer mieszkania"),
        }
        # fields = ['country', 'city', 'post_code', 'street', 'building_no', 'appartment_no']

UserAddressFormSet = inlineformset_factory(
    parent_model=models.User, 
    model=models.Address, 
    form=AddressForm, 
    extra=0,
    min_num=1,
    can_delete=False,
)

class OrderForm(ModelForm):
    class Meta:
        model = models.Order
        exclude = ['id', 'order_value', 'payment_status', 'declared_order_duration']
        widgets = {
            'customer': TextInput(attrs={'class': 'mb-3 form-control', 'readonly': True}),
            'car': TextInput(attrs={'class': 'mb-3 form-control', 'readonly': True}),
            'order_value': TextInput(attrs={'class': 'mb-3 form-control'}),
            'declared_order_duration': TextInput(attrs={'class': 'mb-3 form-control'}),
            'pickup_date': DateInput(attrs={'class': 'mb-3 form-control', 'type': 'date'}),
            'return_date': DateInput(attrs={'class': 'mb-3 form-control', 'type': 'date'}),
            'deposit': TextInput(attrs={'class': 'mb-3 form-control', 'readonly': True}),
            'payment_method': Select(attrs={'class': 'mb-3 form-control'}),
            'payment_status': TextInput(attrs={'class': 'mb-3 form-control'}),                    
        }