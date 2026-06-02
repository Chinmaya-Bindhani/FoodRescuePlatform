from django.shortcuts import render
from donation_app.models import Donation


def human_food_view(request):
    context = {
        'human_veg': Donation.objects.filter(food_for='human', food_type='veg', quantity__gt=0).order_by('-created_at'),
        'human_nonveg': Donation.objects.filter(food_for='human', food_type='nonveg', quantity__gt=0).order_by('-created_at'),
    }
    return render(request, 'human_food_app/human_food.html', context)

