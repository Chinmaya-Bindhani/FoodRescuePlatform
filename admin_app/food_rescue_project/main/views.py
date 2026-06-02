from django.shortcuts import render
from food.models import FoodDonation

def home(request):
    latest_human = FoodDonation.objects.filter(category='human').order_by('-created_at')[:4]
    latest_animal = FoodDonation.objects.filter(category='animal').order_by('-created_at')[:4]
    return render(request, 'main/home.html', {
        'latest_human': latest_human,
        'latest_animal': latest_animal,
    })

def about(request):
    return render(request, 'main/about.html')
