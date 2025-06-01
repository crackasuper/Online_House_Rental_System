from django.db import models
from django.contrib.auth.models import User
from properties.models import Property
from django.utils import timezone

class RentalAgreement(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tenant_agreements')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_agreements')
    start_date = models.DateField()
    end_date = models.DateField()
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2)
    terms_and_conditions = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    admin_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    signed_by_tenant = models.BooleanField(default=False)
    signed_by_owner = models.BooleanField(default=False)
    signed_by_admin = models.BooleanField(default=False)
    tenant_signature_date = models.DateTimeField(null=True, blank=True)
    owner_signature_date = models.DateTimeField(null=True, blank=True)
    admin_signature_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Agreement for {self.property.title} - {self.tenant.get_full_name()}"

    def is_fully_signed(self):
        return self.signed_by_tenant and self.signed_by_owner and self.signed_by_admin

    def can_be_approved(self):
        return self.is_fully_signed() and self.status == 'pending'

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='bookings')
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)
    agreement = models.OneToOneField(RentalAgreement, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Booking for {self.property.title} by {self.tenant.email}"

    def get_status_display(self):
        return dict(self.STATUS_CHOICES).get(self.status, self.status)

    class Meta:
        ordering = ['-created_at'] 