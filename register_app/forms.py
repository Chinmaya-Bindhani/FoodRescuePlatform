from django import forms
from .models import Donor


class DonorRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = Donor
        fields = ['first_name', 'last_name', 'email', 'mobile', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Mobile number'}),
        }
