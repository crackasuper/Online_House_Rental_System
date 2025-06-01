from django.urls import path
from . import views

urlpatterns = [
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('create/<int:property_id>/', views.create_booking, name='create_booking'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
] 