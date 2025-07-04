# BookBuddy

# 1. Clone the Repository
git clone https://github.com/your-username/book-buddy-backend.git
cd book-buddy-backend

# 2 & 3. Create virtual environment, activate it, install dependencies, and run the server
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Tech Stack
Python 3.10+ – Core programming language

Django 4.x – Web framework for building robust backend

Django REST Framework (DRF) – For building RESTful APIs

SQLite3 – Default database (can be swapped with PostgreSQL)

CORS Headers – To enable communication with frontend (React)

Django Admin – For managing users, books, and reviews from the admin panel


Features
✅ User Management

User authentication (if implemented)

Admin user via Django admin panel

📚 Book CRUD APIs

Create, retrieve, update, delete books

Store title, author, genre, and status (wishlist/reading/completed)

🌟 Review System

Add ratings and notes to books as reviews

📈 Progress Tracking

Track number of pages read

Update reading progress dynamically

🔎 Filter and Search Support

Filter books by status (wishlist, reading, completed)

Search books by genre

⚙️ RESTful API

Built using Django REST Framework

JSON-based API responses

Easily consumable from frontend (React)