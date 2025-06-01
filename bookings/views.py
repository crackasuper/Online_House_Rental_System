from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import datetime
from .models import Booking
from properties.models import Property

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
        
        messages.success(request, 'Booking request submitted successfully!')
        return redirect('my_bookings')
    
    return redirect('property_detail', pk=property_id)

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