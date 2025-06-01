from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('owner/dashboard/', views.owner_dashboard, name='owner_dashboard'),
] 