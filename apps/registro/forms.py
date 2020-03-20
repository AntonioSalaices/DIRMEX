#coding: utf-8
from django import forms
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib.auth.models import User
from apps.registro.models import Empresas, Participantes
from django.core import validators


class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario",widget=forms.TextInput(attrs={'class':'form-signin-heading'}))
    password = forms.CharField(label="Contraseña",widget=forms.PasswordInput(attrs={'class':'form-signin-heading'}))
    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        if not user:
            raise forms.ValidationError("El usuario no existe")
        if not user.check_password(password):
            raise forms.ValidationError("El usuario o la contraseña son incorrectos")
        return super(LoginForm,self).clean(*args,**kwargs)



class ParticipanteForm(forms.ModelForm):
    imagen = forms.ImageField()
    class Meta:
        model = Participantes
        fields = [
            'nombre', 
            'telefono',
            'telefono2',
            'email',
            'imagen',
            'red_social',
            'estado',
            'municipio',
            'colonia',
        ]
        labels = {
            'nombre': 'Nombre: ',
            'telefono': 'Teléfono: ',
            'telefono2': 'Teléfono 2: ',
            'email': 'Email: ',
            'imagen': 'Imagen: ',
            'estado': 'Estado: ',
            'red_social': 'Red Social: ',
            'municipio': 'Municipio: ',
            'colonia': 'Colonia: ',
        }
        exclude = [
            'num_votos'
        ]

    def clean(self):
        cleaned_data = super().clean()
        nombre = self.cleaned_data.get("nombre")
        telefono =self.cleaned_data.get("telefono")
        telefono2 = self.cleaned_data.get("telefono2")
        email = self.cleaned_data.get("email")
        imagen = self.cleaned_data.get("imagen")
        estado = self.cleaned_data.get("estado")
        red_social = self.cleaned_data.get("red_social")
        municipio = self.cleaned_data.get("municipio")
        colonia = self.cleaned_data.get('colonia')

    def clean_image(self):
        imagen = self.cleaned_data.get('imagen', False)
        if imagen:
            if imagen._size > 4*1024*1024:
                raise ValidationError("Image file too large ( > 4mb )")
            return imagen
        else:
            raise ValidationError("Couldn't read uploaded image")

    
