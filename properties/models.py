from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Property(models.Model):
    PROPERTY_TYPES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('condo', 'Condo'),
        ('villa', 'Villa'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1)
    area = models.PositiveIntegerField(help_text='Area in square feet')
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')

    def __str__(self):
        return self.title

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.property.title}"

class Amenity(models.Model):
    name = models.CharField(max_length=100)
    properties = models.ManyToManyField(Property, related_name='amenities')

    def __str__(self):
        return self.name 