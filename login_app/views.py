from django.contrib import messages
from django.shortcuts import redirect, render
from register_app.models import Donor
from .forms import DonorLoginForm


def login_view(request):
    if request.session.get('donor_id'):
        return redirect('home')

    form = DonorLoginForm()
    error = ''

    if request.method == 'POST':
        form = DonorLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            donor = Donor.objects.filter(email=email, password=password).first()
            if donor:
                request.session['donor_id'] = donor.id
                request.session['donor_name'] = donor.first_name
                messages.success(request, 'Login successful.')
                return redirect('home')
            error = 'Invalid credentials. Please register first.'

    return render(request, 'login_app/login.html', {'form': form, 'error': error})


def logout_view(request):
    request.session.flush()
    messages.success(request, 'Logged out successfully.')
    return redirect('home')
