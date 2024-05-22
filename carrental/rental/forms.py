from django.forms import ModelForm
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