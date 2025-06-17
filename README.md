# Online House Rental System

A full-stack Django-based web application for renting, listing, and managing houses. Built with Python, Django, JavaScript, and HTML/CSS, this system streamlines the process of connecting landlords with tenants.


## 🚀 Features

- 🧾 User registration and authentication
- 🏘️ Landlords can post property listings
- 🔍 Tenants can browse/search/filter available rentals
- 📄 Admin approval system for listings
- 🧠 Smart dashboard for landlords and admins
- Responsive Design

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3)

---

  
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


