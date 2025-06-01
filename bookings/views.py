from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone
from datetime import datetime
from .models import Booking, RentalAgreement
from properties.models import Property
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def create_booking(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        notes = request.POST.get('notes', '')
        
        # Convert string dates to datetime objects
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        
        # Validate dates
        if start_date < timezone.now().date():
            messages.error(request, 'Start date cannot be in the past.')
            return redirect('property_detail', pk=property_id)
        
        if end_date <= start_date:
            messages.error(request, 'End date must be after start date.')
            return redirect('property_detail', pk=property_id)
        
        # Check for overlapping bookings
        overlapping_bookings = Booking.objects.filter(
            property=property,
            status__in=['pending', 'approved'],
            start_date__lte=end_date,
            end_date__gte=start_date
        )
        
        if overlapping_bookings.exists():
            messages.error(request, 'This property is already booked for the selected dates.')
            return redirect('property_detail', pk=property_id)
        
        # Calculate total price
        months = (end_date.year - start_date.year) * 12 + end_date.month - start_date.month
        total_price = property.price * months
        
        # Create booking
        booking = Booking.objects.create(
            property=property,
            tenant=request.user,
            start_date=start_date,
            end_date=end_date,
            total_price=total_price,
            notes=notes
        )
        
        # Create rental agreement
        agreement = RentalAgreement.objects.create(
            property=property,
            tenant=request.user,
            owner=property.owner,
            start_date=start_date,
            end_date=end_date,
            monthly_rent=property.price,
            security_deposit=property.price,  # One month's rent as security deposit
            terms_and_conditions=property.terms_and_conditions or "Standard rental terms and conditions apply.",
            status='pending'
        )
        
        # Link agreement to booking
        booking.agreement = agreement
        booking.save()
        
        messages.success(request, 'Booking request and rental agreement submitted successfully!')
        return redirect('view_agreement', agreement_id=agreement.id)
    
    return redirect('property_detail', pk=property_id)

@login_required
def view_agreement(request, agreement_id):
    agreement = get_object_or_404(RentalAgreement, id=agreement_id)
    
    # Check if user has permission to view
    if not (request.user == agreement.tenant or 
            request.user == agreement.owner or 
            request.user.is_staff):
        messages.error(request, 'You do not have permission to view this agreement.')
        return redirect('home')
    
    return render(request, 'bookings/agreement.html', {
        'agreement': agreement,
        'can_sign': (
            (request.user == agreement.tenant and not agreement.signed_by_tenant) or
            (request.user == agreement.owner and not agreement.signed_by_owner) or
            (request.user.is_staff and not agreement.signed_by_admin)
        )
    })

@login_required
def sign_agreement(request, agreement_id):
    agreement = get_object_or_404(RentalAgreement, id=agreement_id)
    
    if request.method == 'POST':
        if request.user == agreement.tenant and not agreement.signed_by_tenant:
            agreement.signed_by_tenant = True
            agreement.tenant_signature_date = timezone.now()
        elif request.user == agreement.owner and not agreement.signed_by_owner:
            agreement.signed_by_owner = True
            agreement.owner_signature_date = timezone.now()
        elif request.user.is_staff and not agreement.signed_by_admin:
            agreement.signed_by_admin = True
            agreement.admin_signature_date = timezone.now()
            agreement.admin_notes = request.POST.get('admin_notes', '')
        
        agreement.save()
        
        if agreement.is_fully_signed():
            agreement.status = 'approved'
            agreement.save()
            
            # Update booking status
            if agreement.booking:
                agreement.booking.status = 'approved'
                agreement.booking.save()
        
        messages.success(request, 'Agreement signed successfully!')
        return redirect('view_agreement', agreement_id=agreement.id)
    
    return redirect('view_agreement', agreement_id=agreement.id)

@staff_member_required
def admin_agreements(request):
    agreements = RentalAgreement.objects.all().order_by('-created_at')
    return render(request, 'bookings/admin_agreements.html', {
        'agreements': agreements
    })

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(tenant=request.user).order_by('-created_at')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, tenant=request.user)
    
    if booking.status in ['pending', 'approved']:
        booking.status = 'cancelled'
        booking.save()
        messages.success(request, 'Booking cancelled successfully.')
    else:
        messages.error(request, 'This booking cannot be cancelled.')
    
    return redirect('my_bookings') 