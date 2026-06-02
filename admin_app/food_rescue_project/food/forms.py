from django import forms
from .models import FoodDonation

class FoodDonationForm(forms.ModelForm):
    class Meta:
        model = FoodDonation
        fields = ['title', 'description', 'category', 'food_type', 'quantity', 'location']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
