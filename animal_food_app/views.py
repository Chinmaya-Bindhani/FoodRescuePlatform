from django.shortcuts import render
from donation_app.models import Donation


def animal_food_view(request):
    context = {
        'animal_food': Donation.objects.filter(food_for='animal', quantity__gt=0).order_by('-created_at')
    }
    return render(request, 'animal_food_app/animal_food.html', context)
