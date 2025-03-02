from django import forms
from .models import Carteira

class CarteiraForm(forms.ModelForm):
    class Meta:
        model = Carteira
        fields = ['saldo', 'moeda']