from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import FoodDonationForm
from .models import FoodDonation

@login_required
def dashboard(request):
    my_items = FoodDonation.objects.filter(donor=request.user)
    return render(request, 'food/dashboard.html', {'my_items': my_items})

@login_required
def create_donation(request):
    if request.method == 'POST':
        form = FoodDonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.donor = request.user
            if donation.category == 'animal':
                donation.food_type = 'animal'
            donation.save()
            return redirect('dashboard')
    else:
        form = FoodDonationForm()
    return render(request, 'food/create_donation.html', {'form': form})

def human_food(request):
    return render(request, 'food/human_food.html')

def human_veg(request):
    items = FoodDonation.objects.filter(category='human', food_type='veg')
    return render(request, 'food/human_veg.html', {'items': items})

def human_nonveg(request):
    items = FoodDonation.objects.filter(category='human', food_type='nonveg')
    return render(request, 'food/human_nonveg.html', {'items': items})

def animal_food(request):
    items = FoodDonation.objects.filter(category='animal')
    return render(request, 'food/animal_food.html', {'items': items})
