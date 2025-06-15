# Online House Rental System

A web-based platform for house rentals built with Django, JavaScript, Bootstrap, HTML, and CSS.

## Features

- User Authentication (Sign up, Login, Logout)
- Property Listings
- Property Search and Filtering
- Property Booking System
- User Dashboard
- Admin Panel
- Responsive Design

  
## Screenshots for

- Home Screen
- ![image alt](https://github.com/crackasuper/Online_House_Rental_System/blob/4c279b49336979fc2780e49ad09eeb9c328bdbf2/homepages.png)
- Login
- ![image alt](https://github.com/crackasuper/Online_House_Rental_System/blob/2e06dab064fc2ac2499d69e895a0d8abea434126/login.png)
- Owners property dashboard
- ![image alt](https://github.com/crackasuper/Online_House_Rental_System/blob/ffcd9ad77a1b01168c601092492d508387811f3e/ownership%20property.png)
- Tenants Booking
- ![image alt](https://github.com/crackasuper/Online_House_Rental_System/blob/5c61cd54cfaf1a78af9fe9aea789492f5ce4fd82/booking.png)
- Properties and filtering
- ![image alt](https://github.com/crackasuper/Online_House_Rental_System/blob/58e920cf2e784fd8d09fa603db15d686eb0616f3/127.0.0.1_8000_property_1_.png)

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate  # On Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

6. Visit http://127.0.0.1:8000/ to access the application

## Project Structure

- `rental_system/` - Main Django project directory
- `properties/` - Property management app
- `accounts/` - User authentication app
- `bookings/` - Booking management app
- `static/` - Static files (CSS, JS, images)
- `templates/` - HTML templates
- `media/` - User-uploaded files

## Technologies Used

- Django 5.0.2
- Bootstrap 5
- JavaScript
- HTML5
- CSS3
- SQLite (Development) / PostgreSQL (Production) 
