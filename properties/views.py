from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib import messages
from .models import Property, PropertyImage
from django.views.generic import ListView, DetailView, CreateView
from .forms import PropertyForm
from django.urls import reverse_lazy

def home(request):
    featured_properties = Property.objects.filter(is_featured=True)[:6]
    latest_properties = Property.objects.all().order_by('-created_at')[:10]
    context = {
        'featured_properties': featured_properties,
        'latest_properties': latest_properties,
    }
    return render(request, 'home.html', context)

class PropertyListView(ListView):
    model = Property
    template_name = 'properties/property_list.html'
    context_object_name = 'properties'
    paginate_by = 9

    def get_queryset(self):
        queryset = Property.objects.all()
        city = self.request.GET.get('city')
        property_type = self.request.GET.get('property_type')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        bedrooms = self.request.GET.get('bedrooms')

        if city:
            queryset = queryset.filter(city__icontains=city)
        if property_type:
            queryset = queryset.filter(property_type=property_type)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if bedrooms:
            queryset = queryset.filter(bedrooms__gte=bedrooms)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['property_types'] = Property.PROPERTY_TYPES
        return context

class PropertyDetailView(DetailView):
    model = Property
    template_name = 'properties/property_detail.html'
    context_object_name = 'property'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.images.all()
        context['amenities'] = self.object.amenities.all()
        return context

@login_required
def my_properties(request):
    properties = Property.objects.filter(owner=request.user)
    return render(request, 'properties/my_properties.html', {'properties': properties})

@login_required
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.owner = request.user
            property.save()
            
            # Handle multiple images
            images = request.FILES.getlist('images')
            for image in images:
                PropertyImage.objects.create(
                    property=property,
                    image=image,
                    is_primary=not PropertyImage.objects.filter(property=property).exists()
                )
            
            messages.success(request, 'Property added successfully!')
            return redirect('property_detail', pk=property.pk)
    else:
        form = PropertyForm()
    
    return render(request, 'properties/add_property.html', {'form': form})

@login_required
def owner_dashboard(request):
    properties = Property.objects.filter(owner=request.user)
    return render(request, 'properties/owner_dashboard.html', {
        'properties': properties,
        'total_properties': properties.count(),
        'available_properties': properties.filter(is_available=True).count()
    })

@login_required
def edit_property(request, pk):
    property = get_object_or_404(Property, pk=pk, owner=request.user)
    
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            property = form.save()
            
            # Handle multiple images
            images = request.FILES.getlist('images')
            for image in images:
                PropertyImage.objects.create(
                    property=property,
                    image=image,
                    is_primary=not PropertyImage.objects.filter(property=property).exists()
                )
            
            messages.success(request, 'Property updated successfully!')
            return redirect('property_detail', pk=property.pk)
    else:
        form = PropertyForm(instance=property)
    
    return render(request, 'properties/edit_property.html', {
        'form': form,
        'property': property
    }) 