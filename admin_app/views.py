from django.shortcuts import render
from donation_app.models import Donation
from register_app.models import Donor


def admin_page_view(request):
    donations = Donation.objects.select_related('donor').order_by('-created_at')
    context = {
        'donor_count': Donor.objects.count(),
        'donation_count': Donation.objects.count(),
        'available_count': Donation.objects.filter(quantity__gt=0).count(),
        'donations': donations,
    }
    return render(request, 'admin_app/admin_page.html', context)


