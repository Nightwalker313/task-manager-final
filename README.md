Task Manager App - README Instructions
Date: May 16, 2025
Author: Amen Ziyad
 
-What the App Does

This is a personal Task Management Web Application built with Django. It allows users to:
- Register and securely log in
- Create, view, update, and delete their personal tasks
- Track due dates and prioritize tasks
- Stay organized through a clean, user-friendly interface

 How to Run It

1. Clone the repository:
   git clone https://github.com/Nightwalker313/task-manager-final.git
   cd task-manager-final

2. Create and activate a virtual environment:
   python -m venv venv
   venv\Scripts\activate   (on Windows)

3. Install the requirements:
   pip install -r requirements.txt

4. Run the Django server:
   python manage.py runserver

-How to Create a Superuser (Admin Account)

Before logging in, you'll need to create a superuser account by running:
   python manage.py createsuperuser

Follow the prompts to enter a username, email, and password.

 How to Log In

1. Start the server with: python manage.py runserver
2. Visit: http://127.0.0.1:8000/login/
3. Enter your superuser credentials
4. You’ll be redirected to your personal task dashboard



