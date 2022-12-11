from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegistroUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
class PortafolioForm(forms.Form):
    titulo = forms.CharField(max_length=200)
    descripcion = forms.CharField(max_length=250)
    foto = forms.URLField()
    url = forms.URLField(label='Ingresa url de la ubicación imagen')
    tags = forms.CharField(max_length=100)

