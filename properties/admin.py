from django.contrib import admin
from .models import Property, PropertyImage, Amenity

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

class AmenityInline(admin.TabularInline):
    model = Property.amenities.through
    extra = 1

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'property_type', 'city', 'price', 'is_available', 'owner')
    list_filter = ('property_type', 'is_available', 'city', 'state')
    search_fields = ('title', 'description', 'address', 'city', 'state')
    inlines = [PropertyImageInline, AmenityInline]
    exclude = ('amenities',)

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',) 