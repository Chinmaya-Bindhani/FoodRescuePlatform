from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import DonorRegisterForm


def register_view(request):
    if request.session.get('donor_id'):
        return redirect('home')

    form = DonorRegisterForm()
    if request.method == 'POST':
        form = DonorRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Please login.')
            return redirect('login')
    return render(request, 'register_app/register.html', {'form': form})
