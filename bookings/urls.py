from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:property_id>/', views.create_booking, name='create_booking'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('agreement/<int:agreement_id>/', views.view_agreement, name='view_agreement'),
    path('agreement/<int:agreement_id>/sign/', views.sign_agreement, name='sign_agreement'),
    path('admin/agreements/', views.admin_agreements, name='admin_agreements'),
] 