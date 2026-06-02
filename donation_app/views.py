from django.contrib import messages
from django.db.models import F
from django.shortcuts import get_object_or_404, redirect, render
from register_app.models import Donor
from .forms import DonationForm
from .models import Donation, Claim
from math import radians, sin, cos, sqrt, atan2
from django.http import JsonResponse
import requests


def donate_view(request):
    donor_id = request.session.get('donor_id')
    if not donor_id:
        messages.error(request, 'Please login first.')
        return redirect('login')

    donor = get_object_or_404(Donor, id=donor_id)
    form = DonationForm()
    if request.method == 'POST':
        form = DonationForm(request.POST, request.FILES)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.donor = donor
            donation.save()
            messages.success(request, 'Donation submitted successfully.')
            return redirect('home')

    return render(request, 'donation_app/donate.html', {'form': form})


def get_address(request):
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')

    if not lat or not lng:
        return JsonResponse({'address': ''})

    url = f"https://api-bdc.net/data/reverse-geocode-client?latitude={lat}&longitude={lng}&localityLanguage=en"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        place = (
            data.get("city")
            or data.get("locality")
            or data.get("principalSubdivision")
            or data.get("localityInfo", {}).get("administrative", [{}])[-1].get("name")
            or ""
        )

        return JsonResponse({'address': place})

    except Exception as e:
        return JsonResponse({'address': '', 'error': str(e)})


def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


def nearby_food(request):
    user_lat = request.GET.get('latitude')
    user_lng = request.GET.get('longitude')

    nearby_items = []

    if user_lat and user_lng:
        user_lat = float(user_lat)
        user_lng = float(user_lng)

        donations = Donation.objects.filter(
            quantity__gt=0,
            latitude__isnull=False,
            longitude__isnull=False
        )

        for item in donations:
            distance = haversine(user_lat, user_lng, item.latitude, item.longitude)
            nearby_items.append((distance, item))

        nearby_items.sort(key=lambda x: x[0])

    return render(request, 'donation_app/nearby_food.html', {'nearby_items': nearby_items})

from django.utils import timezone

def claim_food(request, donation_id):
    if request.method != "POST":
        return redirect('home')

    donor_id = request.session.get('donor_id')
    if not donor_id:
        messages.error(request, "You have to login or register first to claim food.")
        return redirect('login')

    donor = get_object_or_404(Donor, id=donor_id)
    donation = get_object_or_404(Donation, id=donation_id)

    if donation.food_for == "animal":
        claim_category = "animal"
    elif donation.food_type == "veg":
        claim_category = "veg"
    else:
        claim_category = "nonveg"

    today = timezone.now().date()

    total_claims = Claim.objects.filter(
        donor=donor,
        category=claim_category,
        claimed_at__date=today
    ).count()

    if total_claims >= 5:
        messages.error(request, f"You can claim only 5 {claim_category} foods per day.")
        return redirect(request.META.get('HTTP_REFERER', 'home'))

    updated_rows = Donation.objects.filter(
        id=donation.id,
        quantity__gt=0
    ).update(quantity=F('quantity') - 1)

    if updated_rows == 0:
        messages.error(request, "This food is no longer available.")
        return redirect(request.META.get('HTTP_REFERER', 'home'))

    Claim.objects.create(
        donor=donor,
        donation=donation,
        category=claim_category
    )

    messages.success(request, "Food claimed successfully.")
    return redirect(request.META.get('HTTP_REFERER', 'home'))