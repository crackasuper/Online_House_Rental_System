from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from properties.models import Property

@login_required
def profile(request):
    if request.method == 'POST':
        # Update user information
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.save()

        # Update profile information
        profile = request.user.profile
        profile.phone_number = request.POST.get('phone_number', '')
        profile.address = request.POST.get('address', '')
        profile.role = request.POST.get('role', 'tenant')
        
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']
        
        profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')

    return render(request, 'accounts/profile.html')

@login_required
def owner_dashboard(request):
    if not request.user.profile.is_property_owner:
        messages.error(request, 'You must be a property owner to access this page.')
        return redirect('profile')
    
    properties = Property.objects.filter(owner=request.user)
    return render(request, 'accounts/owner_dashboard.html', {
        'properties': properties,
        'total_properties': properties.count(),
        'available_properties': properties.filter(is_available=True).count()
    }) 