from django import forms
from .models import Donation


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['food_for', 'food_type', 'food_name', 'quantity', 'location', 'image', 'latitude', 'longitude']
        widgets = {
            'food_name': forms.TextInput(attrs={'placeholder': 'Food name'}),
            'quantity': forms.NumberInput(attrs={'min': 1, 'placeholder': 'Quantity'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }
