from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.PropertyListView.as_view(), name='property_list'),
    path('property/<int:pk>/', views.PropertyDetailView.as_view(), name='property_detail'),
    path('my-properties/', views.my_properties, name='my_properties'),
    path('owner/dashboard/', views.owner_dashboard, name='owner_dashboard'),
    path('property/add/', views.add_property, name='add_property'),
    path('property/<int:pk>/edit/', views.edit_property, name='edit_property'),
] 