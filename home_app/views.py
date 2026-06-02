from django.shortcuts import render
from donation_app.models import Donation


def home_view(request):
    context = {
        'human_veg': Donation.objects.filter(food_for='human', food_type='veg', quantity__gt=0).order_by('-created_at')[:6],
        'human_nonveg': Donation.objects.filter(food_for='human', food_type='nonveg', quantity__gt=0).order_by('-created_at')[:6],
        'animal_food': Donation.objects.filter(food_for='animal', quantity__gt=0).order_by('-created_at')[:6],
    }
    return render(request, 'home_app/home.html', context)
