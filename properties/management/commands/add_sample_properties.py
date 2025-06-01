from django.core.management.base import BaseCommand
from properties.models import Property, PropertyImage, Amenity
from django.core.files import File
from django.utils import timezone
import requests
from io import BytesIO
import random
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Adds sample properties to the database'

    def handle(self, *args, **kwargs):
        # Sample property data
        properties_data = [
            {
                'title': 'Modern Downtown Apartment',
                'description': 'Beautiful modern apartment in the heart of downtown. Features high ceilings, large windows, and modern appliances.',
                'address': '123 Main St',
                'city': 'New York',
                'state': 'NY',
                'zip_code': '10001',
                'price': 2500,
                'bedrooms': 2,
                'bathrooms': 2,
                'area': 1200,
                'property_type': 'apartment',
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267'
            },
            {
                'title': 'Luxury Villa with Pool',
                'description': 'Stunning luxury villa with private pool, garden, and modern amenities. Perfect for those seeking privacy and comfort.',
                'address': '456 Palm Ave',
                'city': 'Miami',
                'state': 'FL',
                'zip_code': '33101',
                'price': 5000,
                'bedrooms': 4,
                'bathrooms': 3,
                'area': 3000,
                'property_type': 'villa',
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1613977257363-707ba9348227'
            },
            {
                'title': 'Cozy Family House',
                'description': 'Spacious family house in a quiet neighborhood. Large backyard, modern kitchen, and plenty of storage space.',
                'address': '789 Oak St',
                'city': 'Chicago',
                'state': 'IL',
                'zip_code': '60601',
                'price': 3500,
                'bedrooms': 3,
                'bathrooms': 2,
                'area': 2000,
                'property_type': 'house',
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1568605114967-8130f3a36994'
            },
            {
                'title': 'Waterfront Condo',
                'description': 'Luxurious waterfront condo with amazing views. Features modern design, high-end finishes, and access to private beach.',
                'address': '101 Ocean Dr',
                'city': 'Los Angeles',
                'state': 'CA',
                'zip_code': '90210',
                'price': 4000,
                'bedrooms': 2,
                'bathrooms': 2,
                'area': 1500,
                'property_type': 'condo',
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1545324418-cc1a3fa10c00'
            },
            {
                'title': 'Urban Loft',
                'description': 'Stylish urban loft in the arts district. Open floor plan, exposed brick walls, and modern industrial design.',
                'address': '202 Art St',
                'city': 'San Francisco',
                'state': 'CA',
                'zip_code': '94105',
                'price': 3000,
                'bedrooms': 1,
                'bathrooms': 1,
                'area': 1000,
                'property_type': 'apartment',
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1502672260266-1c1ef2d93688'
            }
        ]

        # Sample amenities
        amenities = [
            'Swimming Pool',
            'Gym',
            'Parking',
            'Air Conditioning',
            'High-Speed Internet',
            'Washer/Dryer',
            'Dishwasher',
            'Balcony',
            'Security System',
            'Pet Friendly'
        ]

        # Create amenities
        for amenity_name in amenities:
            Amenity.objects.get_or_create(name=amenity_name)

        # Get the first user as owner
        owner = User.objects.first()
        if not owner:
            self.stdout.write(self.style.ERROR('No user found. Please create a user first.'))
            return

        # Create properties
        for prop_data in properties_data:
            # Download and save image
            response = requests.get(prop_data['image_url'])
            if response.status_code == 200:
                image_file = BytesIO(response.content)
                image_file.name = f"{prop_data['title'].lower().replace(' ', '_')}.jpg"

                # Create property
                property = Property.objects.create(
                    title=prop_data['title'],
                    description=prop_data['description'],
                    address=prop_data['address'],
                    city=prop_data['city'],
                    state=prop_data['state'],
                    zip_code=prop_data['zip_code'],
                    price=prop_data['price'],
                    bedrooms=prop_data['bedrooms'],
                    bathrooms=prop_data['bathrooms'],
                    area=prop_data['area'],
                    property_type=prop_data['property_type'],
                    is_featured=prop_data['is_featured'],
                    created_at=timezone.now(),
                    owner=owner
                )

                # Add image
                PropertyImage.objects.create(
                    property=property,
                    image=File(image_file)
                )

                # Add random amenities
                random_amenities = random.sample(amenities, random.randint(3, 6))
                for amenity_name in random_amenities:
                    amenity = Amenity.objects.get(name=amenity_name)
                    property.amenities.add(amenity)

                self.stdout.write(self.style.SUCCESS(f'Successfully created property "{property.title}"'))
            else:
                self.stdout.write(self.style.ERROR(f'Failed to download image for "{prop_data["title"]}"')) 