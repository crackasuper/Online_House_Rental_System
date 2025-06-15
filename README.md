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
- Tenants Bookings
  
## Screenshots for
-Tenants Booking
-Properties and filtering
![image alt](https://github.com/crackasuper/Online_House_Rental_System/blob/cc88e02c6a4049c5b124cff5c9b1713de752b69c/127.0.0.1_8000_properties_%20(2).png)

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
