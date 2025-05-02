# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Correo Electrónico", required=True)
    first_name = forms.CharField(label="Nombre", max_length=100, required=False)
    last_name = forms.CharField(label="Apellido", max_length=100, required=False)

    class Meta(UserCreationForm.Meta):
        model = User # Especifica el modelo User
        # Campos que se mostrarán (username y passwords vienen de UserCreationForm)
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email

# Formulario para EDITAR campos básicos del modelo User
class UserUpdateForm(forms.ModelForm):
    # Hacemos el email requerido si no lo es por defecto en UserChangeForm
    email = forms.EmailField(label="Correo Electrónico", required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

# Formulario para EDITAR campos del modelo Profile
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        # Especifica los campos del modelo Profile para editar
        fields = ('avatar', 'bio')
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file'}), # Widget para archivos
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Sobre vos...'}),
        }