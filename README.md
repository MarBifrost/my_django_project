# Store and Orders

This project consists of a Django web application that includes two main apps:
- store
- Order
The Store app handles user autorization and also viewing the store page
The Order app manages the ordering process and showing if payment is successful

# Table of Contents
- Technologies Used
- Installation
- Project Structure
- App Details
- URL configuration
- Models
- Forms
- Views
- Templates
- Running the application

  # Technologies Used
  - Python 3.*
  - Django 3.* or above
  - SQlite (default database)
  - HTML/CSS for front-end templates
 

  # Installation
  - Clone the repository
      - git clone https://github.com/MarBifrost/my_django_tasks
  - cd my_django_tasts
  - Install the required packages
      - pip install -r requirements.txt
  - Apply migrations:
      - python manage.py makemigrations
      - python manage.py migrate
   
  # Project structure:

```bash
├── <Store and Orders>/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── store/
│   ├── migrations/
│   ├── templates/
│   │   └── store/
│   │       ├── index.html
│   │       └── login.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
└── order/
    ├── migrations/
    ├── templates/
    │   └── order/
    │       ├── index.html
    │       └── payment_success.html
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
  
```
# App details
- Store app
  Url patterns:
  - /store/: Displays the store index page
  - /store/login/: displays the login page
  - /store/logout/: Logs the user out
 
- Order app
  Url patterns
  - /order/: displays the order index page
  - /order/payment/ : Displays payment success and order placement page
 

# Models

Order Model
The order model represents an order placed by a user. It includes fields for:
- Id - a UUID field serving as the primary key
- Product - a char field for the product name
- name - A char field for user's first name
- last_name -  A char field for user's last name
- phone -  a char field for a user's phone number
- shipping_address: A char field for the fhipping address


# Views
- Store Views:
  - store:
  - login_views
  - logout_views

- Order Views
  -order
  paynment_success

# Templates
-store/templates/store/index.html
-store/templates/store/login.html
-order/templates/order/index.html
-order/templates/order/payment_success.html


# Running the application
-python manage.py runserver
you can access the following pages at following links:
- admin autorization page in your browser at http://127.0.0.1:8000/admin
- autorization to the store page: http://127.0.0.1:8000/store/login/
    - username - 'mariam'
    - password - 'mariam123'
- after a successful login it redirects to the main store page: http://127.0.0.1:8000/store/
- From store page you can move to the order page: http://127.0.0.1:8000/order/
- At the order page you can click on Place order and find yourself on the 'payment_success' page, or push to the 'Back' button and go back to the store page
- If you'll fill the form on the order page, details of your order will store in product's database. 

